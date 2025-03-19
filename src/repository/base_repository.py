from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from pydantic import BaseModel

from abc import ABC, abstractmethod


class BaseRepository(ABC):

    @abstractmethod
    async def get_all(self) -> Union["BaseModel", None]:
        raise NotImplemented

    @abstractmethod
    async def add(self, item: BaseModel) -> int:
        raise NotImplemented
    