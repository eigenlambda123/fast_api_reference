from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

@app.exception_handler(StarletteHTTPException) # Register the custom exception handler for HTTPException
async def http_exception_handler(request, exc):
    """Custom exception handler for HTTPException."""
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code) # return a plain text response with the error message