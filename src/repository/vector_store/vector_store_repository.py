from typing import Set

import numpy as np

from src.vector_store import BaseRetriever
from src.dto import DirectionMetadata


class VectorStoreRepository:
    def __init__(self, retriever: BaseRetriever):
        self._retriever = retriever
        
    def find_similar(
        self, 
        vector: np.ndarray[float],
        top_n: int = 10,
    ) -> Set[DirectionMetadata]:
        results = self._retriever.retrieve(vector, top_n)
        metadatas = results.get("metadatas")
        return {
            DirectionMetadata.from_metadata(metadata)
            for metadata in metadatas[0]
        }
