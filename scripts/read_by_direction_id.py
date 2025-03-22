import asyncio

from src.database.crud import DirectionCRUD, EntranceExamCRUD, PassingPointsCRUD
from src.database.database_manager import DatabaseManager
from src.config import settings


async def main() -> None:
    direction_crud = DirectionCRUD(DatabaseManager(settings.postgres.url))
    exam_crud = EntranceExamCRUD(DatabaseManager(settings.postgres.url))
    points_crud = PassingPointsCRUD(DatabaseManager(settings.postgres.url))

    direction = await direction_crud.read_by_direction_id(6)
    print(direction)
    exams = await exam_crud.read_by_direction_id(6)
    print(exams)
    points = await points_crud.read_by_direction_id(6)
    print(points)


asyncio.run(main())
