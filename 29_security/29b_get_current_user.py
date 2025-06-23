from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

# OAuth2PasswordBearer is a class to retrieve the token from the request.
# The tokenUrl parameter is the endpoint where the client would get the token.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    """Pydantic model representing a user in the system."""
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


def fake_decode_token(token):
    """
    Simulate decoding a JWT token and retrieving a user.
    In a real application, you would verify the token and fetch user info from a database.
    """
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    Dependency that extracts the token from the request,
    decodes it, and returns the corresponding user.
    """
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    """
    Endpoint to get the current authenticated user's information.
    The current_user is injected by the get_current_user dependency.
    """
    return current_user