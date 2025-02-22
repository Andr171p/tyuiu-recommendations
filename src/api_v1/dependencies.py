from src.api_v1.container import Container
from src.core.use_cases import RecommendationsUseCase


container = Container()


def get_recommendations_use_case() -> RecommendationsUseCase:
    return container.recommendations_use_case()
