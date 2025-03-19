from src.repository import PointsRepository
from src.core.entities import PointsHistory


class PointsUseCase:
    def __init__(self, points_repository: PointsRepository) -> None:
        self.points_repository = points_repository

    async def get_by_direction_id(self, direction_id: int) -> PointsHistory:
        points = await self.points_repository.get_by_direction_id(direction_id)
        return PointsHistory(
            history=[point for point in points]
        )
