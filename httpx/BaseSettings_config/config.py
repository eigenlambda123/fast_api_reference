from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    weather_api_key: str
    model_config = SettingsConfigDict(env_file=".env") # Automatically load environment variables from .env file

settings = Settings()