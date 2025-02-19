from src.dto import ApplicantDTO
from src.core.entities import Recommendations, Direction
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

    def recommend(self, applicant_dto: ApplicantDTO) -> Recommendations:
        dataframe = applicant_dto.to_dataframe()
        vector = self._preprocessing_service.preprocess(dataframe)
        print(vector)
        directions_dto = self._retriever_service.find_similar_directions(vector[0])
        return Recommendations(
            directions=[
                Direction(**direction_dto.model_dump())
                for direction_dto in directions_dto
            ]
        )
