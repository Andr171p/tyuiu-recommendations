import uuid
from importlib.metadata import metadata

import joblib
import chromadb
import pandas as pd
from pathlib import Path


BASE_DIR: Path = Path(__file__).resolve().parent.parent

CHROMA_PATH: Path = BASE_DIR / "chroma"

DATAFRAME_PATH: Path = BASE_DIR / "scripts" / "Processed_Applicants.csv"

SCALER_PATH: Path = BASE_DIR / "estimators" / "applicants_scaler.joblib"


chroma_client = chromadb.PersistentClient(path=str(CHROMA_PATH))
collection = chroma_client.get_or_create_collection("applicants")

df = pd.read_csv(DATAFRAME_PATH)
df.drop("Unnamed: 0",axis=1, inplace=True)

applicants = df.drop("direction", axis=1)
directions = df["direction"]

scaler = joblib.load(SCALER_PATH)

scaled_applicants = scaler.transform(applicants)

'''for vector, direction in zip(scaled_applicants, directions):
    collection.add(
        ids=[str(uuid.uuid4())],
        embeddings=[vector.tolist()],
        metadatas={
            "name": direction,
            "description": "",
            "link": ""
        }
    )
'''

results = collection.query(
    query_embeddings=scaled_applicants[1000]
)
metadatas = results["metadatas"]
print(len(metadatas[0]))
unique_names = set()
for metadata in metadatas[0]:
    unique_names.add(metadata["name"])

print(unique_names)
print(len(unique_names))