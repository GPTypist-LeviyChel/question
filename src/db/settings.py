from pydantic import BaseSettings
import os

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db = os.getenv("DB_NAME")


class PostgresDBSettings(BaseSettings):
    POSTGRES_URI = f"postgres://{user}:{password}@{host}:{port}/{db}"
