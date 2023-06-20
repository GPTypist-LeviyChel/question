import os
from src.db.settings import PostgresDBSettings


configs = [PostgresDBSettings]


class Settings(*configs):
    API_URL: str = "/questions"
    API_KEY: str = os.getenv("API_KEY")


settings = Settings()
