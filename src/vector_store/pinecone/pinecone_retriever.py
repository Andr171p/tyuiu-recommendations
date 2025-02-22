from numpy import ndarray
from pinecone import Pinecone

from src.vector_store.base_retriever import BaseRetriever


class PineconeRetriever(BaseRetriever):
    def __init__(
            self,
            pinecone: Pinecone,
            index_name: str,
    ) -> None:
        self._index = pinecone.Index(index_name)

    def retrieve(
            self,
            vector: ndarray[float],
            top_n: int = 10
    ) -> dict:
        results = self._index.query(
            vector=vector[0].tolist(),
            top_k=top_n,
            include_metadata=True
        )
        return results
