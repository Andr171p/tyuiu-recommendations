from typing import Literal, List

from pydantic import BaseModel

from src.core.entities.entrance_exams import EntranceExam


class Direction(BaseModel):
    direction_id: int
    education_form: Literal["ОФО", "ЗФО"]
    name: str
    description: str
    
    class Config:
        from_attributes = True
