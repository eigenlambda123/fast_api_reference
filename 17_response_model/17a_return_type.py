from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item: # Specifying return type Item
    """Create an item and return it."""
    return item


@app.get("/items/")
async def read_items() -> list[Item]: # Specifying return type list[Item]
    """Return a list of items."""
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]