from typing import Literal, List

from pydantic import BaseModel

from src.core.entities.entrance_exam import EntranceExam


class Direction(BaseModel):
    direction_id: int
    education_form: Literal["ОФО", "ЗФО"]
    name: str
    entrance_exams: List[EntranceExam]
    description: str
    
    class Config:
        from_attributes = True
