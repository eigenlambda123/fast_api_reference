from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/", response_model=Item) # Specify response model instead of return type
async def create_item(item: Item) -> Any: #  Specify return type as Any
    return item


@app.get("/items/", response_model=list[Item]) # Specify response model as a list of Item
async def read_items() -> Any: # Specify return type as Any
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]