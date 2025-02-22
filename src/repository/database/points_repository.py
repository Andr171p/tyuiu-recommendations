from typing import List

from src.repository.database.database_repository import DatabaseRepository
from src.database.models import PointsModel
from src.database.crud import PointsCRUD
from src.core.entities import Points


class PointsRepository(DatabaseRepository):
    def __init__(self, crud: PointsCRUD) -> None:
        self._crud = crud
        
    async def get_all(self) -> List[Points] | None:
        points = await self._crud.read_all()
        return [Points.model_validate(point) for point in points] if points else None
    
    async def get_by_direction_id(self, direction_id: int) -> List[Points] | None:
        points = await self._crud.read_by_direction_id(direction_id)
        return [Points.model_validate(point) for point in points] if points else None
    
    async def add(self, points: Points) -> int:
        id = self._crud.create(PointsModel(**points.model_dump()))
        return id
    