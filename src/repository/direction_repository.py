from typing import List, Union

from src.repository.base_repository import BaseRepository
from src.database.crud import DirectionCRUD
from src.database.models import DirectionModel
from src.core.entities import Direction


class DirectionRepository(BaseRepository):
    def __init__(self, crud: DirectionCRUD) -> None:
        self._crud = crud

    async def add(self, direction: Direction) -> int:
        id = await self._crud.create(DirectionModel(**direction.model_dump()))
        return id
        
    async def get_all(self) -> List[Union[Direction, None]]:
        directions = await self._crud.read_all()
        return [Direction.model_validate(direction) for direction in directions] if directions else []
        
    async def get_by_direction_id(self, direction_id: int) -> Union[Direction, None]:
        direction = await self._crud.read_by_direction_id(direction_id)
        return Direction.model_validate(direction) if direction else None
    