from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent


class TransformersSettings(BaseSettings):
    gender_binarizer_path: Path = BASE_DIR / "fitted_transformers" / "gender_binarizer.joblib"
    military_service_binarizer_path: Path = BASE_DIR / "fitted_transformers" / "military_service_binarizer.joblib"
    foreign_citizenship_encoder_path: Path = BASE_DIR / "fitted_transformers" / "foreign_citizenship_encoder.joblib"
    applicants_scaler_path: Path = BASE_DIR / "fitted_transformers" / "applicants_scaler.joblib"


class ChromaSettings(BaseSettings):
    path: Path = BASE_DIR / "chroma"

class Settings(BaseSettings):
    transformers: TransformersSettings = TransformersSettings()
    chroma: ChromaSettings = ChromaSettings()


settings = Settings()
