from fastapi import FastAPI
from pydantic_settings import BaseSettings


class Settings(BaseSettings): # uses BaseSettings from pydantic_settings
    """Application settings loaded from environment variables"""
    app_name: str = "Awesome API"
    admin_email: str
    items_per_user: int = 50


settings = Settings() # Automatically loads environment variables and validates them
app = FastAPI()


@app.get("/info")
async def info():

    # use the settings object to access configuration values
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }