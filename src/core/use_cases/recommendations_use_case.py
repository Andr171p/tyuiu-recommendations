from src.core.entities import Recommendations, Applicant
from src.repository.vector_store import VectorStoreRepository
from src.services.preprocessing import PreprocessingService


class RecommendationsUseCase:
    def __init__(
            self,
            preprocessing_service: PreprocessingService,
            vector_store_repository: VectorStoreRepository
    ) -> None:
        self._preprocessing_service = preprocessing_service
        self._vector_store_repository = vector_store_repository

    def recommend(self, applicant: Applicant) -> Recommendations:
        preprocessed = self._preprocessing_service.preprocess(applicant)
        directions_metadata = self._vector_store_repository.find_similar(preprocessed)
        return Recommendations.from_directions_metadata(directions_metadata)
