from typing import Set

import numpy as np

from src.repository.vector_store.vector_store_repository import VectorStoreRepository
from src.vector_store import BaseRetriever
from src.dto import DirectionMetadata


class PineconeRepository(VectorStoreRepository):
    def __init__(self, retriever: BaseRetriever) -> None:
        self._retriever = retriever

    def find_similar(
        self,
        vector: np.ndarray[float],
        top_n: int = 10,
    ) -> Set[DirectionMetadata]:
        results = self._retriever.retrieve(vector, top_n)
        metadatas = [match["metadata"] for match in results["matches"]]
        return {
            DirectionMetadata.from_metadata(metadata)
            for metadata in metadatas
        }
