from collections.abc import Mapping

from pydantic import BaseModel


class DirectionMetadata(BaseModel):
    direction_id: int
    name: str

    @classmethod
    def from_metadata(cls, metadata: Mapping) -> "DirectionMetadata":
        return cls(
            direction_id=metadata["direction_id"],
            name=metadata["name"],
        )
        
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __eq__(self, direction: "DirectionMetadata") -> bool:
        if self.name == direction.name and self.description == direction.description:
            return True
        return False
