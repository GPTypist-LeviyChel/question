import os
from src.db.settings import PostgresDBSettings


configs = [PostgresDBSettings]


class Settings(*configs):
    API_URL: str = "/api/v1"


settings = Settings()
db_url = os.getenv("DB_URL")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")


