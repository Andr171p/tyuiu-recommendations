from src.core.entities import Recommendations, Applicant
from src.mappers import ApplicantMapper, RecommendationsMapper
from src.recommendation_system import RecommendationSystem


class RecommendationsUseCase:
    def __init__(self, recommendations_system: RecommendationSystem) -> None:
        self._recommendations_system = recommendations_system

    def recommend(self, applicant: Applicant) -> Recommendations:
        applicant_df = ApplicantMapper.to_df(applicant)
        recommendations = self._recommendations_system.recommend(applicant_df)
        return RecommendationsMapper.from_df(recommendations)
