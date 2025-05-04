import os
from pathlib import Path
from typing import Literal
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent.parent

ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)

CSV_PATH = BASE_DIR / "datasets" / "csv" / "tyuiu_students_with_ids_2019-2024.csv"


class PostgresSettings(BaseSettings):
    pg_host: str = "localhost"
    pg_port: int = 5432
    pg_user: str = os.getenv("POSTGRES_USER")
    pg_password: str = os.getenv("POSTGRES_PASSWORD")
    pg_db: str = os.getenv("POSTGRES_DB")

    driver: Literal["asyncpg"] = "asyncpg"

    @property
    def sqlalchemy_url(self) -> str:
        return f"postgresql+{self.driver}://{self.pg_user}:{self.pg_password}@{self.pg_host}/{self.pg_db}"
