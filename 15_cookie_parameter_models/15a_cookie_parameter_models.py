from typing import Annotated

from fastapi import Cookie, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Cookies(BaseModel):
    """
    Cookies model to read multiple cookies using Pydantic.
    This model defines the expected structure of cookies that can be sent
    """
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@app.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()]): # Read multiple cookies using a Pydantic model
    return cookies