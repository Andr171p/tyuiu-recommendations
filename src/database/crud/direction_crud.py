from typing import Sequence

from sqlalchemy import select

from src.database.models import DirectionModel
from src.database.crud.base_crud import BaseCRUD
from src.database.database_manager import DatabaseManager


class DirectionCRUD(BaseCRUD):
    def __init__(self, manager: DatabaseManager) -> None:
        self._manager = manager
        
    async def create(self, direction: DirectionModel) -> int:
        async with self._manager.session() as session:
            session.add(direction)
            id = direction.id
            await session.commit()
        return id
    
    async def read_by_direction_id(self, direction_id: int) -> Sequence[DirectionModel]:
        async with self._manager.session() as session:
            stmt = (
                select(DirectionModel)
                .where(DirectionModel.direction_id == direction_id)
            )
            direction = await session.execute(stmt)
        return direction.scalar_one_or_none()
    
    async def read_all(self) -> Sequence[DirectionModel]:
        async with self._manager.session() as session:
            stmt = select(DirectionModel)
            directions = await session.execute(stmt)
        return directions.scalars().all()
