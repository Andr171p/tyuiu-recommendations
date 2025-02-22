from typing import List

from pydantic import BaseModel

from src.dto import DirectionMetadata

class Recommendations(BaseModel):
    directions: List[DirectionMetadata]
    
    @classmethod
    def from_directions_metadatas(
        cls, 
        directions_metadata: List[DirectionMetadata]
    ) -> "Recommendations":
        return cls(
            directions=[
                direction_matadata
                for direction_matadata in directions_metadata
            ]
        )
