from typing import Optional

from fastapi import FastAPI

app = FastAPI()


# 데코레이터 문법
# 이거 하나를 라우터라고 함.
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}/{xyz}")
def read_item(item_id: int, xyz: str, q: Optional[str] = None):
    return {"item_id": item_id, "q": q, "xyz": xyz}
