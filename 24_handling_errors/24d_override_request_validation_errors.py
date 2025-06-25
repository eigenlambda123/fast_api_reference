from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.exception_handler(RequestValidationError) # Register the custom exception handler for RequestValidationError
async def validation_exception_handler(request, exc):
    """
    Custom exception handler for RequestValidationError.
    Returns a plain text response with a 400 status code and the error message.
    """
    return PlainTextResponse(str(exc), status_code=400) # Custom handler for RequestValidationError