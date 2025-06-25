from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

class UnicornException(Exception):
    """Custom exception class for Unicorn-related errors."""
    def __init__(self, name: str):
        self.name = name

app = FastAPI()

@app.exception_handler(UnicornException) # Register the custom exception handler for UnicornException
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    """
    Custom exception handler for UnicornException.
    Returns a JSON response with a 418 status code and a custom message.
    """
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )

@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name) # Raise a custom UnicornException
    return {"unicorn_name": name}