from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pandas import DataFrame
    from sklearn.pipeline import Pipeline

from abc import ABC, abstractmethod
from numpy import ndarray


class BasePipeline(ABC):
    _pipeline: "Pipeline"
    
    @abstractmethod
    def transform(self, dataframe: "DataFrame") -> ndarray[float]:
        raise NotImplemented
