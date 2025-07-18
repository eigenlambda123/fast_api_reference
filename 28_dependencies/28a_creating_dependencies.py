from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100): # dependency function
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]): # dependency injection
    return commons


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]): # dependency injection
    return commons