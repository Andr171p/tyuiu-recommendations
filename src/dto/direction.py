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
