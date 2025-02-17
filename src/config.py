from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent


class EstimatorsSettings(BaseSettings):
    ...


class Settings(BaseSettings):
    ...


settings = Settings()
