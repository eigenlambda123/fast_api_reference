from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl # URL of the image with type parameter using HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None # List of Image models with type parameter


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item): 
    results = {"item_id": item_id, "item": item}
    return results