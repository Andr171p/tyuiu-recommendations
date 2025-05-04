from typing import List, Literal

import pandas as pd

from pydantic import BaseModel, Field, field_validator, ConfigDict

from .constants import (
    MIN_GPA,
    MAX_GPA,
    MIN_POINTS,
    MAX_POINTS,
    MIN_EXAM_POINTS,
    MAX_EXAM_POINTS,
    SUBJECTS_MAP
)


class Exam(BaseModel):
    subject: Literal[
        "Русский язык",
        "Обществознание",
        "Математика",
        "Физика",
        "Химия",
        "История",
        "Информатика"
    ]
    points: int = Field(ge=MIN_EXAM_POINTS, le=MAX_EXAM_POINTS)

    @field_validator("subject")
    def validate_subject(
            cls,
            subject: str
    ) -> Literal[
        "russian",
        "social_science",
        "math",
        "physics",
        "chemistry",
        "history",
        "informatics"
    ]:
        return SUBJECTS_MAP[subject]


class Applicant(BaseModel):
    gender: Literal["male", "female"]
    gpa: float = Field(ge=MIN_GPA, le=MAX_GPA)
    points: int = Field(ge=MIN_POINTS, le=MAX_POINTS)
    exams: List[Exam]

    @field_validator("gender")
    def validate_gender(cls, gender: Literal["male", "female"]) -> Literal[0, 1]:
        return 1 if gender == "male" else 0

    @property
    def exams_dict(self) -> dict[str, int]:
        return {exam.subject: exam.points for exam in self.exams}

    def to_df(self) -> pd.DataFrame:
        applicant_dict = {
            "Пол": self.gender,
            "Ср. балл док-та об образовании": self.gpa,
            "Сумма баллов": self.points,
            "Обществознание": self.exams_dict.get("social_science", 0),
            "Математика": self.exams_dict.get("math", 0),
            "Информатика": self.exams_dict.get("informatics", 0),
            "Русский язык": self.exams_dict.get("russian", 0),
            "Физика": self.exams_dict.get("physics", 0),
            "Химия": self.exams_dict.get("chemistry", 0),
            "История": self.exams_dict.get("history", 0)
        }
        return pd.DataFrame([applicant_dict])


class Direction(BaseModel):
    direction_id: int
    education_form: Literal["ОФО", "ЗФО"]
    name: str
    description: str

    model_config = ConfigDict(from_attributes=True)


class RecommendedDirection(BaseModel):
    direction_id: int
    name: str


class EntranceExam(BaseModel):
    priority: int
    name: str
    min_points: int

    model_config = ConfigDict(from_attributes=True)


class PassingPoints(BaseModel):
    year: int
    points: int

    model_config = ConfigDict(from_attributes=True)
