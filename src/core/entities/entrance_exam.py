from pydantic import BaseModel


class EntranceExam(BaseModel):
    priority: int
    name: str
    min_points: int

    class Config:
        from_attributes = True
