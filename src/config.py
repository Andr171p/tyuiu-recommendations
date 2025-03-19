import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


class DatasetSettings(BaseSettings):
    dataset_path: Path = BASE_DIR / "datasets" / "tyuiu_students_with_ids_2019-2024.csv"


class SQLiteSettings(BaseSettings):
    name: str = "db.sqlite3"
    path: Path = BASE_DIR / name
    driver: str = "aiosqlite"
    url: str = f"sqlite+{driver}:///{path}"


class PostgresSettings(BaseSettings):
    user: str = os.getenv("POSTGRES_USER")
    password: str = os.getenv("POSTGRES_PASSWORD")
    host: str = os.getenv("POSTGRES_HOST")
    port: str = os.getenv("POSTGRES_PORT")
    database: str = os.getenv("POSTGRES_DB")

    driver: str = "asyncpg"
    url: str = f"postgresql+{driver}://{user}:{password}@{host}:{port}/{database}"


class Settings(BaseSettings):
    datasets: DatasetSettings = DatasetSettings()
    sqlite: SQLiteSettings = SQLiteSettings()
    postgres: PostgresSettings = PostgresSettings()


settings = Settings()
