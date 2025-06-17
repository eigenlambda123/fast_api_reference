from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None): # Read X-Token from headers with possible duplicates, handling them as a list
    return {"X-Token values": x_token}