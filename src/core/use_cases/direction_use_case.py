from src.repository import DirectionRepository
from src.core.entities import Direction


class DirectionUseCase:
    def __init__(self, direction_repository: DirectionRepository) -> None:
        self._direction_repository = direction_repository

    async def get_by_direction_id(self, direction_id: int) -> Direction:
        direction = await self._direction_repository.get_by_direction_id(direction_id)
        return direction
