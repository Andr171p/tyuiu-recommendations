from pydantic import BaseModel

from src.core.entities.passing_points import PassingPoints


class PassingPointsHistory(BaseModel):
    history: list[PassingPoints]
