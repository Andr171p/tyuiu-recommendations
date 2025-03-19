from dishka import Provider, provide, Scope

from src.recommendation_system import RecommendationSystem
from src.core.use_cases import RecommendationsUseCase
from src.config import settings


class RecommendationsProvider(Provider):
    @provide(scope=Scope.APP)
    def get_recommendation_system(self) -> RecommendationSystem:
        return RecommendationSystem(settings.datasets.dataset_path)

    @provide(scope=Scope.APP)
    def get_recommendations_use_case(
            self,
            recommendation_system: RecommendationSystem
    ) -> RecommendationsUseCase:
        return RecommendationsUseCase(recommendation_system)
