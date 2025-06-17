from pydantic_settings import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    # Base directory settings
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    WORKSPACE_DIR: str = os.path.join(BASE_DIR, "workspace")

    # Database settings
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "refactai"

    # API settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "RefactAI"

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()

# Ensure workspace directory exists
os.makedirs(settings.WORKSPACE_DIR, exist_ok=True)
