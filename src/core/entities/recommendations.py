from typing import List

from pydantic import BaseModel

from src.core.entities.direction import Direction


class Recommendations(BaseModel):
    directions: List[Direction]
