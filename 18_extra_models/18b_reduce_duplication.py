from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserBase(BaseModel):
    """Base model for user data to reduce duplication."""
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    """Model for user input, inheriting from UserBase."""
    password: str


class UserOut(UserBase):
    """Model for user output, inheriting from UserBase."""
    pass


class UserInDB(UserBase):
    """Model for user in the database, inheriting from UserBase."""
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved