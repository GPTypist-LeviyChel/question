from src.db.settings import PostgresDBSettings

configs = [PostgresDBSettings]


class Settings(*configs):
    API_URL: str = "/api/v1"


settings = Settings()