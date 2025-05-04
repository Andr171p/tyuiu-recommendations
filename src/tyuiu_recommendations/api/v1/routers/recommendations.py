from typing import Annotated

from fastapi import APIRouter, status, Depends, Query

from src.tyuiu_recommendations.entities import Applicant
from src.tyuiu_recommendations.constants import MIN_TOP_N, MAX_TOP_N
from src.tyuiu_recommendations.dependencies import get_recommendation_system
from src.tyuiu_recommendations.recommendation_system import RecommendationSystem

from ..schemas import RecommendationsResponse


recommendations_router = APIRouter(
    prefix="/api/v1/recommendations",
    tags=["Recommendations"]
)


@recommendations_router.post(
    path="/{top_n}",
    status_code=status.HTTP_200_OK,
    response_model=RecommendationsResponse
)
async def get_recommendations(
        top_n: Annotated[int, Query(ge=MIN_TOP_N, le=MAX_TOP_N)],
        applicant: Applicant,
        recommendation_system: Annotated[RecommendationSystem, Depends(get_recommendation_system)]
) -> RecommendationsResponse:
    directions = recommendation_system.recommend(applicant, top_n)
    return RecommendationsResponse(directions=directions)
