from fastapi import FastAPI, HTTPException, Query
import httpx
import os
from dotenv import load_dotenv


app = FastAPI()
load_dotenv()


JOKE_API_URL = "https://official-joke-api.appspot.com/random_joke"

@app.get("/joke")
async def get_joke():
    """Fetch a random joke from the official Joke API."""

    try:
        async with httpx.AsyncClient() as client: # Using AsyncClient for asynchronous requests
            response = await client.get(JOKE_API_URL) # Make an asynchronous GET request to the joke API
            response.raise_for_status() # Raise an error for bad responses (4xx or 5xx)

    # Exceptions 
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




GITHUB_API_URL = "https://api.github.com/users/" # Base URL for GitHub API
HEADERS = {"User-Agent": os.getenv("USER_AGENT", "MyApp")} # Default User-Agent header, can be overridden by environment variable

@app.get("/github-user")
async def get_github_user(username: str = Query(..., min_length=1)):
    """Fetch GitHub user information by username"""
    url = f"{GITHUB_API_URL}{username}" # Construct the GitHub API URL for the user

    try:
        async with httpx.AsyncClient() as client: # Using AsyncClient for asynchronous requests
            response = await client.get(url, headers=HEADERS) # Make an asynchronous GET request to the GitHub API
            response.raise_for_status() # Raise an error for bad responses (4xx or 5xx)

    # Exceptions
    except httpx.RequestError as exc:
        raise HTTPException(status_code=500, detail=f"Request error: {exc}")

    except httpx.HTTPStatusError as exc:
        if exc.response.status_code == 404:
            raise HTTPException(status_code=404, detail="GitHub user not found")
        raise HTTPException(status_code=exc.response.status_code, detail="GitHub API error")

    data = response.json() # Parse the JSON response

    # Return relevant user information
    return {
        "login": data.get("login"),
        "name": data.get("name"),
        "public_repos": data.get("public_repos"),
        "followers": data.get("followers"),
        "bio": data.get("bio"),
        "profile_url": data.get("html_url")
    }




API_URL = "https://api.agify.io" # Base URL for the Agify API


@app.get("/predict-age")
async def get_prediction(name: str) -> dict:
    """Fetch age prediction for a given name using the Agify API."""

    params = {"name": name} # Query parameters for the API request

    try:
        async with httpx.AsyncClient(timeout=5.0) as client: # Using AsyncClient for asynchronous requests with a timeout

            response = await client.get(API_URL, params=params) # Make an asynchronous GET request to the Agify API
            print(f"Status Code: {response.status_code}") # Print the status code for debugging
            response.raise_for_status()  # Raise an error for non-200 responses
            data = response.json() # Parse the JSON response
            return data # Return the parsed data
        

    # Exceptions
    except httpx.RequestError as exc:
        print(f"An error occurred while requesting {exc.request.url!r}.")
        return {"error": "Request failed"}
    except httpx.HTTPStatusError as exc:
        print(f"HTTP error {exc.response.status_code}: {exc.response.text}")
        return {"error": "Bad response from server"}