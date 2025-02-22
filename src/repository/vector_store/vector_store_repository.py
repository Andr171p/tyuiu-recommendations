from typing import TYPE_CHECKING, Set

if TYPE_CHECKING:
    from src.vector_store import BaseRetriever
    from src.dto import DirectionMetadata

from abc import ABC, abstractmethod
import numpy as np


class VectorStoreRepository(ABC):
    _retriever: "BaseRetriever"

    @abstractmethod
    def find_similar(
        self, 
        vector: np.ndarray[float],
        top_n: int = 10,
    ) -> Set["DirectionMetadata"]:
        raise NotImplementedError
