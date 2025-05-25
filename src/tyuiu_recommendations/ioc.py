from dishka import Provider, provide, Scope, from_context, make_async_container

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from .constants import STUDENTS_CSV_PATH
from .settings import PostgresSettings
from .recommendation_system import RecommendationSystem
from .database.session import create_sessionmaker
from .database.repositories import DirectionRepository, EntranceExamRepository, PassingPointRepository


class AppProvider(Provider):
    config = from_context(provides=PostgresSettings, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_recommendation_system(self) -> RecommendationSystem:
        return RecommendationSystem(STUDENTS_CSV_PATH)

    @provide(scope=Scope.APP)
    def get_session_maker(self, config: PostgresSettings) -> async_sessionmaker[AsyncSession]:
        return create_sessionmaker(config)

    @provide(scope=Scope.APP)
    def get_direction_repository(
            self,
            session_maker: async_sessionmaker[AsyncSession]
    ) -> DirectionRepository:
        return DirectionRepository(session_maker)

    @provide(scope=Scope.APP)
    def get_entrance_exam_repository(
            self,
            session_maker: async_sessionmaker[AsyncSession]
    ) -> EntranceExamRepository:
        return EntranceExamRepository(session_maker)

    @provide(scope=Scope.APP)
    def get_passing_point_repository(
            self,
            session_maker: async_sessionmaker[AsyncSession]
    ) -> PassingPointRepository:
        return PassingPointRepository(session_maker)


settings = PostgresSettings()

container = make_async_container(AppProvider(), context={PostgresSettings: settings})
