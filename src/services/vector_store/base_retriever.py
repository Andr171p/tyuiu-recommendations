from abc import ABC, abstractmethod
from numpy import ndarray


class BaseRetriever(ABC):
    @abstractmethod
    def retrieve(
            self,
            vector: ndarray[float],
            top_n: int = 10
    ) -> dict:
        raise NotImplemented
