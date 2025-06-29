import httpx
from pydantic import BaseModel, Field
from typing import Optional
import asyncio
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os


app = FastAPI()
load_dotenv()


class WeatherData(BaseModel):
    """Model to represent weather data"""

    location: str # Location name
    country: str # Country name
    temperature_celsius: float # Temperature in Celsius
    condition: str # Weather condition description

    @classmethod
    def from_raw(cls, raw: dict) -> "WeatherData":
        """Create a WeatherData instance from raw API response data"""

        # Return a WeatherData instance with the relevant fields
        return cls(
            location=raw["location"]["name"],
            country=raw["location"]["country"],
            temperature_celsius=raw["current"]["temp_c"],
            condition=raw["current"]["condition"]["text"],
        )
    
@app.get(
    "/weather/{city}",
    response_model=WeatherData, # Specify the response model for automatic validation and serialization
    responses={ 
        404: {"description": "City not found"},
        502: {"description": "Request to weather API failed"},
        500: {"description": "Unexpected server error"},
    }
)
async def fetch_weather(city: str) -> WeatherData:
    """Fetch weather data for a given city using the WeatherAPI"""


    API_URL = "https://api.weatherapi.com/v1/current.json" # Base URL for the WeatherAPI
    API_KEY = os.getenv("WEATHER_API_KEY")
    params = {"key": API_KEY, "q": city} # Query parameters for the API request, including the API key and city name

    try:
        async with httpx.AsyncClient(timeout=5.0) as client: # Using AsyncClient for asynchronous requests with a timeout
            response = await client.get(API_URL, params=params) # Make an asynchronous GET request to the WeatherAPI
            print(f"Status Code: {response.status_code}") # Print the status code for debugging
            response.raise_for_status() # Raise an error for non-200 responses
            raw_data = response.json() # Parse the JSON response
            weather = WeatherData.from_raw(raw_data) # Create a WeatherData instance from the raw data
            return weather # Return the weather data as a WeatherData instance

    # Exceptions
    except httpx.RequestError as exc: # Handle request errors
        return JSONResponse(status_code=502, content={"error": f"Request failed: {exc}"})

    except httpx.HTTPStatusError as exc: # Handle HTTP status errors
        if exc.response.status_code == 404:
            return JSONResponse(status_code=404, content={"error": "City not found"})
        return JSONResponse(status_code=exc.response.status_code, content={"error": f"HTTP error {exc.response.status_code}"})

    except Exception as e: # Handle any other unexpected errors
        return JSONResponse(status_code=500, content={"error": f"Unexpected error: {str(e)}"})
