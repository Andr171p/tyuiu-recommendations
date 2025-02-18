from src.mappers import ApplicantMapper
from src.core.entities import Applicant, Recommendations
from src.core.use_cases import RecommendationsUseCase


class RecommendationsInteration:
    def __init__(self, recommendations_use_case: RecommendationsUseCase) -> None:
        self._recommendations_use_case = recommendations_use_case

    def get_recommendations(self, applicant: Applicant) -> Recommendations:
        applicant_dto = ApplicantMapper.to_dto(applicant)
        recommendations = self._recommendations_use_case.recommend(applicant_dto)
        return recommendations
