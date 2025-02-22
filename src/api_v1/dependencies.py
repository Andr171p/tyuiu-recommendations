from src.api_v1.container import Container
from src.core.use_cases import (
    RecommendationsUseCase,
    DirectionUseCase,
    PointsUseCase,
)


container = Container()


def get_recommendations_use_case() -> RecommendationsUseCase:
    return container.recommendations_use_case()


def get_direction_use_case() -> DirectionUseCase:
    return container.direction_use_case()


def get_points_use_case() -> PointsUseCase:
    return container.points_use_case()
