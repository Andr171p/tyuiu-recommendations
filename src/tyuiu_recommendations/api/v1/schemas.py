from typing import List

from pydantic import BaseModel

from src.tyuiu_recommendations.entities import (
    RecommendedDirection,
    EntranceExam,
    PassingPoints
)


class RecommendationsResponse(BaseModel):
    directions: List[RecommendedDirection]


class EntranceExamsResponse(BaseModel):
    entrance_exams: List[EntranceExam]


class PassingPointsHistoryResponse(BaseModel):
    history: List[PassingPoints]
