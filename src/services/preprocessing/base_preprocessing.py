from abc import ABC, abstractmethod

from pandas import DataFrame
from numpy import ndarray


class BasePreprocessingService(ABC):
    @abstractmethod
    def preprocess(self, dataframe: DataFrame) -> ndarray[float]:
        raise NotImplemented
