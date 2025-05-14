from .settings import PostgresSettings
from .constants import CSV_PATH
from .recommendation_system import RecommendationSystem

from .database.session import create_sessionmaker
from .database.repositories import (
    DirectionRepository,
    EntranceExamRepository,
    PassingPointsRepository
)


sessionmaker = create_sessionmaker(PostgresSettings())


def get_recommendation_system() -> RecommendationSystem:
    return RecommendationSystem(CSV_PATH)


def get_direction_repository() -> DirectionRepository:
    return DirectionRepository(sessionmaker)


def get_entrance_exam_repository() -> EntranceExamRepository:
    return EntranceExamRepository(sessionmaker)


def get_passing_points_repository() -> PassingPointsRepository:
    return PassingPointsRepository(sessionmaker)
