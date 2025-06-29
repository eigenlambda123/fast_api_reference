from fastapi import FastAPI, Query, HTTPException
from typing import Optional
from config import settings # Importing settings from the config module

app = FastAPI()

@app.get("/weather")
async def get_weather_data(
    city: Optional[str] = Query(None, description="City name"),
    lat: Optional[float] = Query(None, description="Latitude"),
    lon: Optional[float] = Query(None, description="Longitude")
):
    """get city or coordinates"""

    # Validate input parameters
    if city is None and (lat is None or lon is None):
        raise HTTPException(status_code=400, detail="You must provide either 'city' or both 'lat' and 'lon'.")

    print(f"API Key from .env: {settings.weather_api_key}") # Debugging line to check if the API key is loaded correctly

    # Dummy return to verify setup works
    if city:
        return {"mode": "city", "query": city}
    else:
        return {"mode": "coordinates", "query": {"lat": lat, "lon": lon}}
