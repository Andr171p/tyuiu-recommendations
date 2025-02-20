import uuid
import joblib
import chromadb
import pandas as pd
from pathlib import Path


BASE_DIR: Path = Path(__file__).resolve().parent.parent

CHROMA_PATH: Path = BASE_DIR / "chroma"

DATAFRAME_PATH: Path = BASE_DIR / "scripts" / "Processed_Applicants.csv"


df = pd.read_csv(DATAFRAME_PATH)
directions_df = df["direction"]
unique_directions = directions_df.unique()

