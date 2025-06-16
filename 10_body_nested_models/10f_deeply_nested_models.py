from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None # List of Image models with type parameter


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item] # List of Item models with type parameter that also contains nested models


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer