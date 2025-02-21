from typing import List

from sqlalchemy import insert, select

from src.services.database.crud.base_crud import BaseCrud
from src.services.database.models import DirectionModel
from src.services.database.database_manager import DatabaseManager


class DirectionCRUD(BaseCrud):
    def __init__(self, manager: DatabaseManager) -> None:
        self._manager = manager
        
    async def create(self, direction: DirectionModel) -> int:
        async with self._manager.session() as session:
            stmt = (
                insert(DirectionModel)
                .values(**direction.__dict__)
                .returning(direction.id)
            )
            id = await session.execute(stmt)
        return id
    
    async def read_by_id(self, id: int) -> DirectionModel | None:
        async with self._manager.session() as session:
            stmt = (
                select(DirectionModel)
                .where(DirectionModel.id == id)
            )
            direction = await session.execute(stmt)
        return direction.scalar_one_or_none()
    
    async def read_by_direction_id(
        self, 
        direction_id: int
    ) -> List[DirectionModel]:
        async with self._manager.session() as session:
            stmt = (
                select(DirectionModel)
                .where(DirectionModel.direction_id == direction_id)
            )
            direction = await session.execute(stmt)
        return direction.scalar_one_or_none()
    
    async def read_all(self) -> List[DirectionModel]:
        async with self._manager.session() as session:
            stmt = select(DirectionModel)
            directions = await session.execute(stmt)
        return directions.scalars().all()
