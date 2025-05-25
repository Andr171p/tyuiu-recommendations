from typing import Literal

import pandas as pd

from pydantic import BaseModel, Field, field_validator, ConfigDict

from .constants import (
    MIN_GPA,
    MAX_GPA,
    MIN_POINTS,
    MAX_POINTS,
    INPUT_EXAMS,
    SUBJECTS_MAP,
    FEATURES_EXAMS,
    MIN_EXAM_POINTS,
    MAX_EXAM_POINTS,
    AVAILABLE_EDUCATION_FORMS,
    DIRECTIONS_MAPPING,
)


class Exam(BaseModel):
    subject: INPUT_EXAMS
    points: int = Field(ge=MIN_EXAM_POINTS, le=MAX_EXAM_POINTS)

    @field_validator("subject")
    def validate_subject(cls, subject: str) -> FEATURES_EXAMS:
        return SUBJECTS_MAP[subject]


class Applicant(BaseModel):
    gender: Literal["male", "female"]
    gpa: float = Field(ge=MIN_GPA, le=MAX_GPA)
    points: int = Field(ge=MIN_POINTS, le=MAX_POINTS)
    exams: list[Exam]

    @field_validator("gender")
    def encode_gender(cls, gender: Literal["male", "female"]) -> Literal[0, 1]:
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
    name: str
    education_form: AVAILABLE_EDUCATION_FORMS
    description: str

    model_config = ConfigDict(from_attributes=True)

    @field_validator("name")
    def mapping_direction_name(cls, name: str) -> str:
        return DIRECTIONS_MAPPING[name]


class Recommendation(BaseModel):
    direction_id: int
    name: str


class EntranceExam(BaseModel):
    name: str
    priority: int
    min_points: int

    model_config = ConfigDict(from_attributes=True)


class PassingPoint(BaseModel):
    year: int
    points: int

    model_config = ConfigDict(from_attributes=True)


class ReadableDirection(Direction):
    entrance_exams: list[EntranceExam]
    passing_points: list[PassingPoint]
