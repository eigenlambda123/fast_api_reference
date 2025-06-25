from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()



@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    """
    Custom exception handler for HTTPException.
    This handler is called when an HTTPException is raised.
    It logs the exception and calls the default HTTP exception handler.
    """
    print(f"OMG! An HTTP error!: {repr(exc)}")
    return await http_exception_handler(request, exc)



@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    """
    Custom exception handler for RequestValidationError.
    This handler is called when a RequestValidationError is raised.
    It logs the exception and calls the default RequestValidationError handler.
    """
    print(f"OMG! The client sent invalid data!: {exc}")
    return await request_validation_exception_handler(request, exc)



@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Endpoint to read an item by its ID.
    Raises an HTTPException if the item ID is 3.
    """
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}