import os
import joblib
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from pinecone import Pinecone

BASE_DIR: Path = Path(__file__).resolve().parent.parent
DATAFRAME_PATH: Path = BASE_DIR / "scripts" / "Processed_Applicants.csv"
SCALER_PATH: Path = BASE_DIR / "fitted_transformers" / "applicants_scaler.joblib"
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(dotenv_path=ENV_PATH)

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index_name = "applicants"
index = pc.Index(index_name)

df = pd.read_csv(DATAFRAME_PATH)
df.drop("Unnamed: 0", axis=1, inplace=True)

applicants = df.drop("direction", axis=1)
directions = df["direction"]

scaler = joblib.load(SCALER_PATH)
scaled_applicants = scaler.transform(applicants)

query_vector = scaled_applicants[10].tolist()
results = index.query(
    vector=query_vector,
    top_k=10,
    include_metadata=True
)
print(results)
metadatas = [match["metadata"] for match in results["matches"]]
print(f"Results found: {len(metadatas)}")
print(metadatas)
