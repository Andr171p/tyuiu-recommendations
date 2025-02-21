from typing import List
from abc import ABC, abstractmethod

from src.services.database.models import BaseModel


class BaseCRUD(ABC):
    @abstractmethod
    async def crate(self, model: BaseModel) -> int:
        raise NotImplemented

    @abstractmethod
    async def read_by_id(self, id: int) -> BaseModel | None:
        raise NotImplemented

    @abstractmethod
    async def read_all(self) -> List[BaseModel] | None:
        raise NotImplemented
