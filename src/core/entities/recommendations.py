from typing import Sequence, List

from pydantic import BaseModel

from src.dto import DirectionMetadata

class Recommendations(BaseModel):
    directions: List[DirectionMetadata]
    
    @classmethod
    def from_directions_metadata(
        cls, 
        directions_metadata: Sequence[DirectionMetadata]
    ) -> "Recommendations":
        return cls(
            directions=[
                direction_metadata
                for direction_metadata in directions_metadata
            ]
        )
