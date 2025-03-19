from typing import List, Union

from src.repository.base_repository import BaseRepository
from src.database.models import PointsModel
from src.database.crud import PointsCRUD
from src.core.entities import Points


class PointsRepository(BaseRepository):
    def __init__(self, crud: PointsCRUD) -> None:
        self._crud = crud

    async def add(self, points: Points) -> int:
        id = await self._crud.create(PointsModel(**points.model_dump()))
        return id
        
    async def get_all(self) -> List[Union[Points, None]]:
        points = await self._crud.read_all()
        return [Points.model_validate(point) for point in points] if points else []
    
    async def get_by_direction_id(self, direction_id: int) -> List[Union[Points, None]]:
        points = await self._crud.read_by_direction_id(direction_id)
        return [Points.model_validate(point) for point in points] if points else []
    