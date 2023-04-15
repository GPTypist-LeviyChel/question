from dataclasses import dataclass


@dataclass
class PostgresDBSettings:
    DB_URL: str = "postgresql://postgres:postgres@localhost:5432/postgres"