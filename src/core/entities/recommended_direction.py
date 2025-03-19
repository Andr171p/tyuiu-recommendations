from pydantic import BaseModel


class RecommendedDirection(BaseModel):
    direction_id: int
    name: str
