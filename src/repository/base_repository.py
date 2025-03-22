from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from pydantic import BaseModel

from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    async def save(self, model: "BaseModel") -> int:
        raise NotImplemented

    @abstractmethod
    async def get_by_direction_id(self, direction_id: int) -> "BaseModel":
        raise NotImplemented

    @abstractmethod
    async def get_all(self) -> Union["BaseModel", None]:
        raise NotImplemented
    