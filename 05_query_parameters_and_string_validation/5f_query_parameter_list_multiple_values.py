from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None): # use annotated query parameter with list of strings
    query_items = {"q": q}
    return query_items