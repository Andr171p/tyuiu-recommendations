from typing import Sequence

from sqlalchemy import select

from src.database.crud.base_crud import BaseCRUD
from src.database.models import PassingPointsModel
from src.database.database_manager import DatabaseManager


class PassingPointsCRUD(BaseCRUD):
    def __init__(self, manager: DatabaseManager) -> None:
        self._manager = manager
        
    async def create(self, passing_points: PassingPointsModel) -> int:
        async with self._manager.session() as session:
            session.add(passing_points)
            id = passing_points.id
            await session.commit()
        return id
    
    async def read_by_direction_id(self, direction_id: int) -> Sequence[PassingPointsModel]:
        async with self._manager.session() as session:
            stmt = (
                select(PassingPointsModel)
                .where(PassingPointsModel.direction_id == direction_id)
            )
            passing_points = await session.execute(stmt)
        return passing_points.scalars().all()
    
    async def read_all(self) -> Sequence[PassingPointsModel]:
        async with self._manager.session() as session:
            stmt = select(PassingPointsModel)
            passing_points = await session.execute(stmt)
        return passing_points.scalars().all()
