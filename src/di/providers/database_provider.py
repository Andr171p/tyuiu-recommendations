from dishka import Provider, provide, Scope

from src.config import settings
from src.database.database_manager import DatabaseManager
from src.database.crud import DirectionCRUD, EntranceExamCRUD, PassingPointsCRUD


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def get_database_manager(self) -> DatabaseManager:
        return DatabaseManager(settings.postgres.url)

    @provide(scope=Scope.APP)
    def get_direction_crud(self, manager: DatabaseManager) -> DirectionCRUD:
        return DirectionCRUD(manager)

    @provide(scope=Scope.APP)
    def get_entrance_exam_crud(self, manager: DatabaseManager) -> EntranceExamCRUD:
        return EntranceExamCRUD(manager)

    @provide(scope=Scope.APP)
    def get_passing_points_crud(self, manager: DatabaseManager) -> PassingPointsCRUD:
        return PassingPointsCRUD(manager)

