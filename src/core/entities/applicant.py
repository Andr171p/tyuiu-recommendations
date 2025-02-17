from typing import List, Literal, Dict

from pydantic import BaseModel

from src.core.entities.exam import Exam


class Applicant(BaseModel):
    gender: Literal["male", "female"]
    foreign_citizenship: str
    military_service: Literal["yes", "no"]
    gpa: float
    points: int
    bonus_points: int
    exams: List[Exam]

    @property
    def exams_dict(self) -> Dict[str, int]:
        return {exam.subject: exam.points for exam in self.exams}
