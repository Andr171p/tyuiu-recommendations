from abc import ABC, abstractmethod

from numpy import ndarray


class BaseRetriever(ABC):
    @abstractmethod
    def find_similar(self, vector: ndarray[float], top_n: int) -> dict:
        raise NotImplemented
