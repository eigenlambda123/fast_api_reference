from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.post("/items/", response_model=Item, tags=["items"]) # Assign the "items" tag to this path operation
async def create_item(item: Item):
    return item


@app.get("/items/", tags=["items"]) # Assign the "items" tag to this path operation
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["users"]) # Assign the "users" tag to this path operation
async def read_users():
    return [{"username": "johndoe"}]