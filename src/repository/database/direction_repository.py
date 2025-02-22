from typing import List

from src.repository.database.database_repository import DatabaseRepository
from src.database.crud import DirectionCRUD
from src.database.models import DirectionModel
from src.core.entities import Direction


class DirectionRepository(DatabaseRepository):
    def __init__(self, crud: DirectionCRUD) -> None:
        self._crud = crud
        
    async def get_all(self) -> List[Direction] | None:
        directions = await self._crud.read_all()
        return [
            Direction.model_validate(direction) 
            for direction in directions
        ]
        
    async def get_by_direction_id(self, direction_id: int) -> Direction | None:
        direction = await self._crud.read_by_direction_id(direction_id)
        return Direction.model_validate(direction) if direction else None
        
    async def add(self, direction: Direction) -> int | None:
        id = await self._crud.create(DirectionModel(**direction.model_dump()))
        return id
    