from typing import List

from pydantic import BaseModel

from src.dto import DirectionMetadata


class Recommendations(BaseModel):
    directions: List[DirectionMetadata]
