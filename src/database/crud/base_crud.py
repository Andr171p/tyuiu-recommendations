from typing import Sequence, Union
from abc import ABC, abstractmethod

from src.database.models import BaseModel


class BaseCRUD(ABC):
    @abstractmethod
    async def create(self, model: BaseModel) -> int:
        raise NotImplemented

    @abstractmethod
    async def read_by_direction_id(self, id: int) -> Union[BaseModel, None]:
        raise NotImplemented

    @abstractmethod
    async def read_all(self) -> Union[Sequence[BaseModel], None]:
        raise NotImplemented
