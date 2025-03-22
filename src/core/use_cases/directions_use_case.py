from src.repository import (
    DirectionRepository,
    EntranceExamRepository,
    PassingPointsRepository,
)
from src.core.entities import (
    Direction,
    PassingPointsHistory,
    EntranceExamsSortByPriority
)


class DirectionsUseCase:
    def __init__(
            self,
            direction_repository: DirectionRepository,
            passing_points_repository: PassingPointsRepository,
            entrance_exam_repository: EntranceExamRepository
    ) -> None:
        self._direction_repository = direction_repository
        self._passing_points_repository = passing_points_repository
        self._entrance_exam_repository = entrance_exam_repository

    async def get_by_direction_id(self, direction_id: int) -> Direction:
        direction = await self._direction_repository.get_by_direction_id(direction_id)
        return direction

    async def get_passing_points_history(self, direction_id: int) -> PassingPointsHistory:
        passing_points = await self._passing_points_repository.get_by_direction_id(direction_id)
        return PassingPointsHistory.from_passing_points(passing_points)

    async def get_entrance_exams(self, direction_id: int) -> EntranceExamsSortByPriority:
        entrance_exams = await self._entrance_exam_repository.get_by_direction_id(direction_id)
        return EntranceExamsSortByPriority.from_entrance_exams(entrance_exams)
