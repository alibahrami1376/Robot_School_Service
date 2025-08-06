from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    BOT_TOKEN: str
    DB_NAME: str = "school_service.db"
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = "./.env"  # مسیر فایل .env
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    return Settings()
