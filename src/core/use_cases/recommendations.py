from src.core.entities import Applicant, Recommendation
from src.dto import ApplicantDTO
from src.services.database import BaseRetriever
from src.services.preprocessing import BasePipeline


class RecommendationsUseCase:
    def __init__(
            self,
            pipeline: BasePipeline,
            retriever: BaseRetriever
    ) -> None:
        self._pipeline = pipeline
        self._retriever = retriever

    def recommend(self, applicant: Applicant) -> Recommendation:
        dataframe = ApplicantDTO.from_applicant(applicant)
        vector = self._pipeline.preprocess(dataframe)
        similar = self._retriever.find_similar(vector)
        return Recommendation(
            directions=[]
        )
