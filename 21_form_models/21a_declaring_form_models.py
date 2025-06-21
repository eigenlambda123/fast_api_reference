from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()


class FormData(BaseModel):
    """Model for form data."""
    username: str
    password: str


@app.post("/login/")
async def login(data: Annotated[FormData, Form()]): # Use Form() to declare form data
    return data