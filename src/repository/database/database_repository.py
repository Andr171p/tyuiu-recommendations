from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.services.database.crud import BaseCRUD

from abc import ABC, abstractmethod
from pydantic import BaseModel


class DatabaseRepository(ABC):
    _crud: "BaseCRUD"
    
    @abstractmethod
    async def get_all(self) -> BaseModel | None:
        raise NotImplemented
    
    @abstractmethod
    async def add(self, item: BaseModel) -> int | None:
        raise NotImplemented
    