from numpy import ndarray
from pandas import DataFrame
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline

from src.preprocessing.base_pipeline import BasePipeline


class SklearnPipeline(BasePipeline):
    def __init__(self, **kwargs: BaseEstimator) -> None:
        self._pipeline = Pipeline([
            (name, estimator)
            for name, estimator in kwargs.items()
        ])

    def transform(self, dataframe: DataFrame) -> ndarray[float]:
        trasformed = self._pipeline.transform(dataframe)
        return trasformed
