from dishka import Provider, provide, Scope

from src.core.use_cases import DirectionsUseCase
from src.database.crud import DirectionCRUD, EntranceExamCRUD, PassingPointsCRUD
from src.repository import DirectionRepository, EntranceExamRepository, PassingPointsRepository


class DirectionsProvider(Provider):
    @provide(scope=Scope.APP)
    def get_direction_repository(self, crud: DirectionCRUD) -> DirectionRepository:
        return DirectionRepository(crud)

    @provide(scope=Scope.APP)
    def get_entrance_exam_repository(self, crud: EntranceExamCRUD) -> EntranceExamRepository:
        return EntranceExamRepository(crud)

    @provide(scope=Scope.APP)
    def get_passing_points_repository(self, crud: PassingPointsCRUD) -> PassingPointsRepository:
        return PassingPointsRepository(crud)

    @provide(scope=Scope.APP)
    def get_directions_use_case(
            self,
            direction_repository: DirectionRepository,
            entrance_exam_repository: EntranceExamRepository,
            passing_points_repository: PassingPointsRepository
    ) -> DirectionsUseCase:
        return DirectionsUseCase(
            direction_repository=direction_repository,
            entrance_exam_repository=entrance_exam_repository,
            passing_points_repository=passing_points_repository
        )
