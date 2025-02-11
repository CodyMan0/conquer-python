from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from app.models import mongodb

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
    return templates.TemplateResponse("./index.html", {"request": request})


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    return templates.TemplateResponse(
        "./index.html", {"request": request, "keyword": q}
    )
