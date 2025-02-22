import asyncio
import pandas as pd
from pathlib import Path

from src.database.models import DirectionModel, PointsModel
from src.database.crud import DirectionCRUD
from src.database.database_manager import DatabaseManager
from src.config import settings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

POINTS_DATAFRAME_PATH: Path = BASE_DIR / "notebooks" / "Проходные баллы 2019-2024.csv"

DIRECTIONS_DATAFRAME_PATH: Path = BASE_DIR / "notebooks" / "Processed_Directions.csv"


def load_csv_to_df(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.drop("Unnamed: 0", axis=1, inplace=True)
    return df


def get_points_model_by_direction_name(direction_name: str) -> list[PointsModel]:
    direction_points_df = points_df[points_df["direction_name"] == direction_name]
    direction_points_df.drop("direction_name", axis=1, inplace=True)
    return [PointsModel(**row.to_dict()) for _, row in direction_points_df.iterrows()]


points_df = load_csv_to_df(POINTS_DATAFRAME_PATH)
directions_df = load_csv_to_df(DIRECTIONS_DATAFRAME_PATH)


async def add_direction_to_db() -> None:
    manager = DatabaseManager(settings.postgres.url)
    crud = DirectionCRUD(manager)
    for _, direction in directions_df.iterrows():
        direction_model = DirectionModel(
            direction_id=int(direction["direction_id"]),
            name=direction["name"],
            description=direction["description"],
            points=get_points_model_by_direction_name(direction["name"])
        )
        await crud.create(direction_model)


asyncio.run(add_direction_to_db())
