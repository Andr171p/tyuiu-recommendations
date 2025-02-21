from abc import ABC, abstractmethod

from src.services.database.models import BaseModel


class BaseCrud(ABC):
    @abstractmethod
    async def crate(self, model: BaseModel) -> int:
        raise NotImplemented

    @abstractmethod
    async def read(self, id: int) -> BaseModel:
        raise NotImplemented

    @abstractmethod
    async def read_all(self) -> list[BaseModel]:
        raise NotImplemented
