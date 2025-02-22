from typing import Literal, Optional

from pandas import DataFrame
from pydantic import BaseModel


class ApplicantDTO(BaseModel):
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

    def to_dataframe(self) -> DataFrame:
        return DataFrame([self.model_dump()])
