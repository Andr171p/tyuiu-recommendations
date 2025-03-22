from typing import List

from pydantic import BaseModel


class EntranceExam(BaseModel):
    priority: int
    name: str
    min_points: int

    class Config:
        from_attributes = True


class EntranceExamsSortByPriority(BaseModel):
    entrance_exams: List[EntranceExam]

    @classmethod
    def from_entrance_exams(cls, entrance_exams: List[EntranceExam]) -> "EntranceExamsSortByPriority":
        return cls(entrance_exams=entrance_exams)
