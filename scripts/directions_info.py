import uuid
import joblib
import chromadb
import pandas as pd
from pathlib import Path


BASE_DIR: Path = Path(__file__).resolve().parent.parent

CHROMA_PATH: Path = BASE_DIR / "chroma"

APPLICANTS_DF_PATH: Path = BASE_DIR / "scripts" / "Processed_Applicants.csv"

DIRECTIONS_DF_PATH: Path = BASE_DIR / "notebooks" / "ТИУ Направления подготовки Бакалавриат.csv"

SCALER_PATH: Path = BASE_DIR / "fitted_transformers" / "applicants_scaler.joblib"


directions_df = pd.read_csv(DIRECTIONS_DF_PATH)
applicants_df = pd.read_csv(APPLICANTS_DF_PATH)
applicants_directions_df = applicants_df["direction"]
applicants_df.drop(["Unnamed: 0", "direction"], axis=1, inplace=True)


scaler = joblib.load(SCALER_PATH)
scaled_applicants = scaler.transform(applicants_df)


chroma_client = chromadb.PersistentClient(path=str(CHROMA_PATH))
# chroma_client.delete_collection("applicants")
collection = chroma_client.get_or_create_collection("applicants")


for vector, direction in zip(scaled_applicants, applicants_directions_df):
    description = directions_df[directions_df["name"] == direction]
    description_text = description["description"].values[0] if not description.empty else ""
    collection.add(
        ids=[str(uuid.uuid4())],
        embeddings=[vector.tolist()],
        metadatas={
            "name": direction,
            "description": description_text
        }
    )
