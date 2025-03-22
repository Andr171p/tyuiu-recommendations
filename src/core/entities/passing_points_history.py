from typing import List

from pydantic import BaseModel

from src.core.entities.passing_points import PassingPoints


class PassingPointsHistory(BaseModel):
    history: List[PassingPoints]

    @classmethod
    def from_passing_points(cls, passing_points: List[PassingPoints]) -> "PassingPointsHistory":
        return cls(history=passing_points)
