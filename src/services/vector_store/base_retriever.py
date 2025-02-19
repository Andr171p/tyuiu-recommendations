from abc import ABC, abstractmethod
from typing import Sequence
from numpy import ndarray

from src.dto import DirectionDTO


class BaseRetrieverService(ABC):
    @abstractmethod
    def find_similar_directions(
            self,
            vector: ndarray[float],
            top_n: int = 10
    ) -> Sequence[DirectionDTO]:
        raise NotImplemented
