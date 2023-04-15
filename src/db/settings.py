from pydantic import BaseSettings
import os

# password = os.getenv("DB_PASSWORD")
password = "contentDB223"

class PostgresDBSettings(BaseSettings):
    POSTGRES_URI = f"postgres://postgres:{password}@159.223.16.147:5432/postgres"