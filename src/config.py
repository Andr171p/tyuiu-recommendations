import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_FILE_PATH: Path = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_FILE_PATH)


class TransformersSettings(BaseSettings):
    gender_binarizer_path: Path = (
            BASE_DIR /
            "fitted_transformers" /
            "gender_binarizer.joblib"
    )
    military_service_binarizer_path: Path = (
            BASE_DIR /
            "fitted_transformers" /
            "military_service_binarizer.joblib"
    )
    foreign_citizenship_encoder_path: Path = (
            BASE_DIR /
            "fitted_transformers" /
            "foreign_citizenship_encoder.joblib"
    )
    applicants_scaler_path: Path = (
            BASE_DIR /
            "fitted_transformers" /
            "applicants_scaler.joblib"
    )


class ChromaSettings(BaseSettings):
    path: Path = BASE_DIR / "chroma"


class PineconeSettings(BaseSettings):
    api_key: str = os.getenv("PINECONE_API_KEY")


class SQLiteSettings(BaseSettings):
    name: str = "db.sqlite3"
    path: Path = BASE_DIR / name
    driver: str = "aiosqlite"
    url: str = f"sqlite+{driver}:///{path}"


class Settings(BaseSettings):
    transformers: TransformersSettings = TransformersSettings()
    chroma: ChromaSettings = ChromaSettings()
    pinecone: PineconeSettings = PineconeSettings()
    sqlite: SQLiteSettings = SQLiteSettings()


settings = Settings()


print(settings.sqlite.url)