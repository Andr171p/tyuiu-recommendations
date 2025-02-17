from typing import List

from numpy import ndarray
from pandas import DataFrame
from sklearn.base import BaseEstimator

from src.services.preprocessing.base import BasePipeline


class PreprocessingPipeline(BasePipeline):
    def __init__(self, estimators: List[BaseEstimator]) -> None:
        self._estimators = estimators

    def preprocess(self, dataframe: DataFrame) -> ndarray[float]:
        ...
