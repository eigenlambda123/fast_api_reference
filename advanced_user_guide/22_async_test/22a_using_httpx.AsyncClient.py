import pytest
from httpx import AsyncClient
from .main import app

@pytest.mark.asyncio
async def test_read_main():
    """
    Test the main endpoint of the FastAPI application using AsyncClient
    """
    
    # Create an instance of AsyncClient with the FastAPI app
    # and a base URL for testing
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Send a GET request to the root endpoint
        response = await ac.get("/")
    assert response.status_code == 200 # Check if the response status code is 200 OK
    assert response.json() == {"msg": "Hello World"} # Check if the response JSON matches the expected output