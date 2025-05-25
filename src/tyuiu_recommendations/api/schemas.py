from pydantic import BaseModel

from ..domain import Recommendation, EntranceExam, PassingPoint


class RecommendationsResponse(BaseModel):
    recommendations: list[Recommendation]


class EntranceExamsResponse(BaseModel):
    entrance_exams: list[EntranceExam]


class PassingPointsResponse(BaseModel):
    passing_points: list[PassingPoint]
