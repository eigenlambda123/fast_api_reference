from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # OAuth2PasswordBearer is a class that provides a way to handle OAuth2 password flow

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]): # Annotated is used to specify that the token parameter should be obtained from the OAuth2PasswordBearer dependency
    return {"token": token}