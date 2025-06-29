from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

JOKE_API_URL = "https://official-joke-api.appspot.com/random_joke"

@app.get("/joke")
async def get_joke():
    """Fetch a random joke from the official Joke API."""

    try:
        async with httpx.AsyncClient() as client: # Using AsyncClient for asynchronous requests
            response = await client.get(JOKE_API_URL) # Make an asynchronous GET request to the joke API
            response.raise_for_status() # Raise an error for bad responses (4xx or 5xx)

    except httpx.RequestError as exc:
        raise HTTPException(status_code=500, detail=f"Request error: {exc}")

    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=f"Error from joke API")


    joke_data = response.json() # Parse the JSON response

    # Return the joke data
    return {
        "setup": joke_data.get("setup"),
        "punchline": joke_data.get("punchline"),
        "source": "official-joke-api"
    }
