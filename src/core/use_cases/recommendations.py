from src.dto import ApplicantVector
from src.mappers import ApplicantMapper
from src.core.entities import Recommendations, Direction, Applicant
from src.services.vector_store import BaseRetrieverService
from src.services.preprocessing import BasePreprocessingService


class RecommendationsUseCase:
    def __init__(
            self,
            preprocessing_service: BasePreprocessingService,
            retriever_service: BaseRetrieverService
    ) -> None:
        self._preprocessing_service = preprocessing_service
        self._retriever_service = retriever_service

    def recommend(self, applicant: Applicant) -> Recommendations:
        applicant_vector = ApplicantMapper.to_applicant_vector(applicant)
        dataframe = applicant_vector.to_dataframe()
        vector = self._preprocessing_service.preprocess(dataframe)
        directions_dto = self._retriever_service.find_similar_directions(vector[0])
        return Recommendations(
            directions=[
                Direction(**direction_dto.model_dump())
                for direction_dto in directions_dto
            ]
        )
