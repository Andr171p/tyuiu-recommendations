from src.api_v1.container import Container
from src.interations import RecommendationsInteration


container = Container()


def get_recommendations_interaction() -> RecommendationsInteration:
    return container.recommendations_interaction()
