from abc import ABC, abstractmethod
from typing import List
from numpy import ndarray

from src.dto import DirectionDTO


class BaseRetrieverService(ABC):
    @abstractmethod
    def find_similar_directions(
            self,
            vector: ndarray[float],
            top_n: int = 10
    ) -> List[DirectionDTO]:
        raise NotImplemented
