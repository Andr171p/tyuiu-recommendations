import asyncio

from src.services.database.database_manager import DatabaseManager
from src.services.database.crud import DirectionCRUD
from src.repository.database.direction_repository import DirectionRepository
from src.config import settings


async def main() -> None:
    manager = DatabaseManager()
    manager.init(settings.sqlite.url)
    crud = DirectionCRUD(manager)
    repository = DirectionRepository(crud)
    direction = await repository.get_by_direction_id(5)
    print(direction)
    
    
asyncio.run(main())
