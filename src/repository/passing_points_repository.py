from typing import List, Union

from src.repository.base_repository import BaseRepository
from src.database.models import PassingPointsModel
from src.database.crud import PassingPointsCRUD
from src.core.entities import PassingPoints


class PassingPointsRepository(BaseRepository):
    def __init__(self, crud: PassingPointsCRUD) -> None:
        self._crud = crud

    async def save(self, points: PassingPoints) -> int:
        id = await self._crud.create(PassingPointsModel(**points.model_dump()))
        return id
        
    async def get_all(self) -> List[Union[PassingPoints, None]]:
        passing_points = await self._crud.read_all()
        return [
            PassingPoints.model_validate(passing_point)
            for passing_point in passing_points
        ] if passing_points else []
    
    async def get_by_direction_id(self, direction_id: int) -> List[Union[PassingPoints, None]]:
        passing_points = await self._crud.read_by_direction_id(direction_id)
        return [
            PassingPoints.model_validate(passing_point)
            for passing_point in passing_points
        ] if passing_points else []
    