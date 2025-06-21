from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()


class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"} # Forbid extra fields in the form data


@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data