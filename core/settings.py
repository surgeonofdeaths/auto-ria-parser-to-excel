from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    URL: str
    FIELDS: list[str]
    CSV_NAME: str
    ANY: bool
    CONSOLE: bool
    MIN_PRICE: int
    MAX_PRICE: int
    MAX_RACE: int
    MIN_YEAR: int
    LOCATION: list[str]
    PAGES: int
    SOLD: bool
    PREFERRED_MARKS: list[str]

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


# read .env and create config only once
@lru_cache()
def get_config():
    config = Settings()
    return config


config = get_config()
