import os
import uuid
import joblib
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from concurrent.futures import ThreadPoolExecutor


BASE_DIR: Path = Path(__file__).resolve().parent.parent

APPLICANTS_DIRECTIONS_DF_PATH: Path = BASE_DIR / "notebooks" / "Applicants_With_Direction.csv"

SCALER_PATH: Path = BASE_DIR / "fitted_transformers" / "applicants_scaler.joblib"

ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(dotenv_path=ENV_PATH)


applicants_directions_df = pd.read_csv(APPLICANTS_DIRECTIONS_DF_PATH)

if applicants_directions_df["direction_id"].isna().any():
    print("Обнаружены пропущенные значения в столбце 'direction_id'. Заполняем их значением по умолчанию (0).")
    applicants_directions_df["direction_id"] = applicants_directions_df["direction_id"].fillna(0)

directions_df = applicants_directions_df[["direction_name", "direction_id"]]
applicants_df = applicants_directions_df.drop(
    ["Unnamed: 0", "direction_name", "direction_id", "description"],
    axis=1,
)

scaler = joblib.load(SCALER_PATH)
scaled_applicants = scaler.transform(applicants_df)


pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index_name = "applicants"
if index_name in pc.list_indexes().names():
    print(f"Index '{index_name}' already exists...")
else:
    pc.create_index(
        name=index_name,
        dimension=scaled_applicants.shape[1],
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )
    print(f"Index '{index_name}' created.")

index = pc.Index(index_name)

print(f"Index '{index_name}' loaded.")
print("Start adding vectors to index.")


batch_size = 100
vectors_batch = []

def upsert_batch(index, batch):
    index.upsert(vectors=batch)

with ThreadPoolExecutor(max_workers=10) as executor:
    for idx, applicant_row in applicants_directions_df.iterrows():
        vector = scaled_applicants[idx]
        direction = directions_df.iloc[idx]
        record_id = str(uuid.uuid4())
        metadata = {
            "name": str(direction["direction_name"]),
            "direction_id": int(direction["direction_id"])
        }
        vectors_batch.append({
            "id": record_id,
            "values": vector.tolist(),
            "metadata": metadata
        })

        if len(vectors_batch) >= batch_size:
            executor.submit(upsert_batch, index, vectors_batch.copy())
            vectors_batch.clear()

    if vectors_batch:
        executor.submit(upsert_batch, index, vectors_batch.copy())

print("Vectors added successfully.")
