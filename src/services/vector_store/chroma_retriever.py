from typing import List, Set

from numpy import ndarray
from chromadb import ClientAPI

from src.dto import DirectionDTO
from src.services.vector_store.base_retriever import BaseRetrieverService


class ChromaRetrieverService(BaseRetrieverService):
    def __init__(
            self,
            client_api: ClientAPI,
            collection_name: str
    ) -> None:
        self._collection = client_api.get_collection(collection_name)

    def find_similar_directions(
            self,
            vector: ndarray[float],
            top_n: int = 10
    ) -> Set[DirectionDTO]:
        results = self._collection.query(
            query_embeddings=[vector.tolist()],
            n_results=top_n
        )
        metadatas = results.get("metadatas")
        return {
            DirectionDTO.from_metadata(metadata)
            for metadata in metadatas[0]
        }
