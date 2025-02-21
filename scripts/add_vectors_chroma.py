import uuid
import joblib
import chromadb
import pandas as pd
from pathlib import Path


BASE_DIR: Path = Path(__file__).resolve().parent.parent

CHROMA_PATH: Path = BASE_DIR / "chroma"

APPLICANTS_DIRECTIONS_DF_PATH: Path = BASE_DIR / "notebboks" / "Applicants_With_Direction.csv"

SCALER_PATH: Path = BASE_DIR / "fitted_transformers" / "applicants_scaler.joblib"


applicants_directions_df = pd.read_csv(r"C:\Users\andre\IdeaProjects\TyuiuDirectionsRecSys\notebooks\Applicants_With_Direction.csv")
directions_df = applicants_directions_df[["direction_name", "direction_id"]]
applicants_df = applicants_directions_df.drop(
    ["Unnamed: 0", "direction_name", "direction_id", "description"], 
    axis=1, 
)


scaler = joblib.load(SCALER_PATH)
scaled_applicants = scaler.transform(applicants_df)


chroma_client = chromadb.PersistentClient(path=str(CHROMA_PATH))
chroma_client.delete_collection("applicants")
collection = chroma_client.get_or_create_collection("applicants")


for idx, applicant_row in applicants_directions_df.iterrows():
    vector = scaled_applicants[idx]
    direction = directions_df.iloc[idx]
    
    collection.add(
        ids=[str(uuid.uuid4())],
        embeddings=[vector.tolist()],
        metadatas={
            "name": direction["direction_name"],
            "direction_id": direction["direction_id"]
        }
    )
