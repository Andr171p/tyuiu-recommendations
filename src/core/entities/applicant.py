from typing import List, Literal, Dict

from pydantic import BaseModel, field_validator

from src.core.entities.exam import Exam


class Applicant(BaseModel):
    gender: Literal["male", "female"]
    gpa: float
    points: int
    exams: List[Exam]

    @field_validator("gender")
    def validate_gender(cls, gender: Literal["male", "female"]) -> Literal[0, 1]:
        return 1 if gender == "male" else 0

    @property
    def exams_dict(self) -> Dict[str, int]:
        return {exam.subject: exam.points for exam in self.exams}

