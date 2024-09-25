# config/settings.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite+aiosqlite:///./integrated_communication.db"
    # Add other configuration settings as needed

    class Config:
        env_file = ".env"