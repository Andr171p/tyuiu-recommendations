from typing import Optional
from collections.abc import Mapping

from pydantic import BaseModel


class DirectionMetadata(BaseModel):
    direction_id: Optional[int]
    name: str

    @classmethod
    def from_metadata(cls, metadata: Mapping) -> "DirectionMetadata":
        return cls(
            direction_id=metadata.get("direction_id"),
            name=metadata.get("name"),
        )
        
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __eq__(self, direction_metadata: "DirectionMetadata") -> bool:
        if self.name == direction_metadata.name:
            return True
        return False
