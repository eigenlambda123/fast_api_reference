from enum import Enum

from fastapi import FastAPI

app = FastAPI()


class Tags(Enum):
    """Enum for API tags."""
    items = "items"
    users = "users"


@app.get("/items/", tags=[Tags.items]) # Assign the "items" tag to this path operation with an Enum
async def get_items():
    return ["Portal gun", "Plumbus"]


@app.get("/users/", tags=[Tags.users]) # Assign the "users" tag to this path operation with an Enum
async def read_users():
    return ["Rick", "Morty"]