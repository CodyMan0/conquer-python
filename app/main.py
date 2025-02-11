from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from app.book_scraper import NaverBookScraper
from app.models import mongodb
from app.models.book import BookModel

DATABASE_URL = "mongodb://localhost:27017"


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("DB 연결 중")
    await mongodb.connect()
    yield
    await mongodb.close()
    print("DB 연결 헤제")


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(lifespan=lifespan)
print(BASE_DIR)

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    context = {"request": request, "title": "데이터 수집가"}
    return templates.TemplateResponse("./index.html", context=context)


@app.get("/search", response_class=HTMLResponse)
async def search_result(request: Request):
    keyword = request.query_params.get("q")  # 쿼리에서 키워드 추출
    if not keyword:  # 키워드가 없다면 사용자에게 검색을 요구
        context = {"request": request}
        return templates.TemplateResponse("index.html", context=context)
    if await mongodb.engine.find_one(BookModel, BookModel.keyword == keyword):
        # 키워드에 대해 수집된 데이터가 DB에 존재한다면 해당 데이터를 사용자에게 보여준다.
        books = await mongodb.engine.find(BookModel, BookModel.keyword == keyword)
        context = {"request": request, "keyword": keyword, "books": books}
        return templates.TemplateResponse("index.html", context=context)
    naver_book_scraper = NaverBookScraper()  # 수집기 인스턴스
    books = await naver_book_scraper.search(keyword, 10)  # 데이터 수집
    book_models = []
    for (
        book
    ) in books:  # 수집된 각각의 데이터에 대해서 DB에 들어갈 모델 인스턴스를 찍는다.
        book_model = BookModel(
            keyword=keyword,
            publisher=book["publisher"],
            price=book.get("price", 0),
            image=book["image"],
        )
        book_models.append(book_model)
    await mongodb.engine.save_all(book_models)  # 각 모델 인스턴스를 DB에 저장한다.
    context = {"request": request, "keyword": keyword, "books": books}
    return templates.TemplateResponse("index.html", context=context)
