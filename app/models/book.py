from odmantic import Model


class BookModel(Model):
    keyword: str
    publisher: str
    price: int
    image: str

    model_config = {"collection": "books"}  # Pydantic v2 스타일
