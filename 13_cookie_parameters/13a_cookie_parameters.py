from typing import Annotated
from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None): # Read ads_id from cookie
    return {"ads_id": ads_id} 