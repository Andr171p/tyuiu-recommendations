from typing import Literal, Optional

import pandas as pd

from src.core.entities import Applicant


class ApplicantDTO(pd.DataFrame):
    _metadata = [
        'gender',
        'foreign_citizenship',
        'military_service',
        'gpa',
        'points',
        'bonus_points',
        'russian',
        'social_science',
        'math',
        'physics',
        'chemistry',
        'history',
        'informatics'
    ]

    gender: Literal["male", "female"]
    foreign_citizenship: str
    military_service: Literal["yes", "no"]
    gpa: float
    points: int
    bonus_points: int
    russian: Optional[int]
    social_science: Optional[int]
    math: Optional[int]
    physics: Optional[int]
    chemistry: Optional[int]
    history: Optional[int]
    informatics: Optional[int]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.gender = kwargs.get("gender")
        self.foreign_citizenship = kwargs.get("foreign_citizenship")
        self.military_service = kwargs.get("military_service")
        self.gpa = kwargs.get("gpa")
        self.points = kwargs.get("points")
        self.bonus_points = kwargs.get("bonus_points")
        self.russian = kwargs.get("russian")
        self.social_science = kwargs.get("social_science")
        self.math = kwargs.get("math")
        self.physics = kwargs.get("physics")
        self.chemistry = kwargs.get("chemistry")
        self.history = kwargs.get("history")
        self.informatics = kwargs.get("informatics")

    @classmethod
    def from_applicant(cls, applicant: Applicant) -> "ApplicantDTO":
        return cls(
            gender=applicant.gender,
            foreign_citizenship=applicant.foreign_citizenship,
            military_service=applicant.military_service,
            gpa=applicant.gpa,
            points=applicant.points,
            bonus_points=applicant.bonus_points,
            russian=applicant.exams_dict.get("russian"),
            social_science=applicant.exams_dict.get("social_science"),
            math=applicant.exams_dict.get("math"),
            physics=applicant.exams_dict.get("physics"),
            chemistry=applicant.exams_dict.get("chemistry"),
            history=applicant.exams_dict.get("history"),
            informatics=applicant.exams_dict.get("informatics")
        )
