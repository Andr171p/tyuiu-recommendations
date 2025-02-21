import asyncio

from src.services.database.database_manager import DatabaseManager
from src.services.database.crud import DirectionCRUD, PointsCRUD
from src.repository.database import DirectionRepository, PointsRepository
from src.config import settings


async def main() -> None:
    manager = DatabaseManager()
    manager.init(settings.sqlite.url)
    direction_repository = DirectionRepository(DirectionCRUD(manager))
    direction = await direction_repository.get_by_direction_id(5)
    points_repository = PointsRepository(PointsCRUD(manager))
    points = await points_repository.get_by_direction_id(5)
    print(direction)
    print(points)
    
    
asyncio.run(main())
