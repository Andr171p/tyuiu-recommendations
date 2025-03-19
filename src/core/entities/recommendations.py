from typing import List

from pydantic import BaseModel

from src.core.entities.recommended_direction import RecommendedDirection


class Recommendations(BaseModel):
    directions: List[RecommendedDirection]
