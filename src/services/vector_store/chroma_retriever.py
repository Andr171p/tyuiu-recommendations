from numpy import ndarray
from chromadb import ClientAPI

from src.services.vector_store.base_retriever import BaseRetrieverService


class ChromaRetrieverService(BaseRetrieverService):
    def __init__(
            self,
            client_api: ClientAPI,
            collection_name: str
    ) -> None:
        self._collection = client_api.get_collection(collection_name)

    def find_similar(
            self,
            vector: ndarray[float],
            top_n: int = 7
    ) -> dict:
        results = self._collection.query(
            query_embeddings=[vector.tolist()],
            n_results=top_n
        )
        return results
