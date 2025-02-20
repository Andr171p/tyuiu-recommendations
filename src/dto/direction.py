from collections.abc import Mapping

from pydantic import BaseModel


class DirectionDTO(BaseModel):
    name: str
    description: str

    @classmethod
    def from_metadata(cls, metadata: Mapping) -> "DirectionDTO":
        return cls(
            name=metadata.get("name"),
            description=metadata.get("description")
        )
        
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __eq__(self, direction: "DirectionDTO") -> bool:
        if self.name == direction.name and self.description == direction.description:
            return True
        return False
