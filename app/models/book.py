from odmantic import Model


class BookModel(Model):
    keyword: str
    publisher: str
    price: int
    image: str

    model_config = {"json_schema_extra": {"example": {"name": "Alice", "age": 30}}}
