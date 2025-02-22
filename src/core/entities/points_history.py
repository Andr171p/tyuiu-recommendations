from pydantic import BaseModel

from src.core.entities.points import Points


class PointsHistory(BaseModel):
    history: list[Points]
