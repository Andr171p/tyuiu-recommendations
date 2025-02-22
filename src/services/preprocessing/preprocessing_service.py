import numpy as np

from src.preprocessing import BasePipeline
from src.mappers import ApplicantMapper
from src.core.entities import Applicant


class PreprocessingService:
    def __init__(self, pipeline: BasePipeline) -> None:
        self._pipeline = pipeline
        
    def preprocess(self, applicant: Applicant) -> np.ndarray[float]:
        applicant_dto = ApplicantMapper.to_dto(applicant)
        dataframe = applicant_dto.to_dataframe()
        preprocessed = self._pipeline.transform(dataframe)
        return preprocessed
