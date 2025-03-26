import asyncio
import pandas as pd

from src.database.models import PassingPointsModel
from src.database.crud import PassingPointsCRUD
from src.database.database_manager import DatabaseManager
from src.config import BASE_DIR, settings


DF_PATH = BASE_DIR / "notebooks" / "ТИУ_проходные_баллы_2014-2024.csv"


df = pd.read_csv(DF_PATH)


async def main() -> None:
    crud = PassingPointsCRUD(DatabaseManager(settings.postgres.url))
    # await truncate_and_reset_id(DatabaseManager(settings.postgres.url), PassingPointsModel())
    for _, row in df.iterrows():
        passing_points_model = PassingPointsModel(
            direction_id=row["ID"],
            year=row["Год"],
            points=row["Сумма баллов"]
        )
        print(passing_points_model)
        try:
            await crud.create(passing_points_model)
        except Exception as _ex:
            print(_ex)


# asyncio.run(main())
