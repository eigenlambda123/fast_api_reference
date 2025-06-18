from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str  # Input-only field
    email: EmailStr

class UserOut(BaseModel):
    username: str  # Output excludes password
    email: EmailStr

@app.post("/user/", response_model=UserOut)  # ← Filters password
async def create_user(user: UserIn) -> Any:
    return user  # Password automatically removed

# @app.post("/user/", response_model=UserOut)  # ← Takes priority
# async def create_user(user: UserIn) -> UserIn:  # ← Ignored by FastAPI
#     return user  # Output filtered to UserOut fields