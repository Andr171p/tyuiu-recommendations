from numpy import ndarray
from pandas import DataFrame
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline

from src.services.preprocessing.base_preprocessing import BasePreprocessingService


class SklearnPreprocessingService(BasePreprocessingService):
    def __init__(self, **kwargs: BaseEstimator) -> None:
        self._pipeline = Pipeline([
            (name, estimator)
            for name, estimator in kwargs.items()
        ])

    def preprocess(self, dataframe: DataFrame) -> ndarray[float]:
        preprocessed = self._pipeline.transform(dataframe)
        return preprocessed
