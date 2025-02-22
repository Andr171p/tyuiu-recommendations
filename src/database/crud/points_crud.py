from typing import List

from sqlalchemy import insert, select

from src.database.crud.base_crud import BaseCRUD
from src.database.models import PointsModel
from src.database.database_manager import DatabaseManager


class PointsCRUD(BaseCRUD):
    def __init__(self, manager: DatabaseManager) -> None:
        self._manager = manager
        
    async def create(self, points: PointsModel) -> int:
        async with self._manager.session() as session:
            stmt = (
                insert(PointsCRUD)
                .values(**points.__dict__)
                .returning(points.id)
            )
            id = await session.execute(stmt)
        return id
    
    async def read_by_id(self, id: int) -> PointsModel:
        async with self._manager.session() as session:
            stmt = (
                select(PointsModel)
                .where(PointsModel.id == id)
            )
            points = await session.execute(stmt)
        return points.scalar_one_or_none()
    
    async def read_by_direction_id(self, direction_id: int) -> List[PointsModel]:
        async with self._manager.session() as session:
            stmt = (
                select(PointsModel)
                .where(PointsModel.direction_id == direction_id)
            )
            points = await session.execute(stmt)
        return points.scalars().all()
    
    async def read_all(self) -> List[PointsModel]:
        async with self._manager.session() as session:
            stmt = select(PointsModel)
            points = await session.execute(stmt)
        return points.scalars().all()
