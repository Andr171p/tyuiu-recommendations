from typing import Annotated

from concurrent.futures import ThreadPoolExecutor

from fastapi import APIRouter, status, Query

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.tyuiu_recommendations.domain import Applicant
from src.tyuiu_recommendations.constants import MIN_TOP_N, MAX_TOP_N
from src.tyuiu_recommendations.recommendation_system import RecommendationSystem

from src.tyuiu_recommendations.api.schemas import RecommendationsResponse


recommendations_router = APIRouter(
    prefix="/api/v1/recommendations",
    tags=["Recommendations"],
    route_class=DishkaRoute
)


@recommendations_router.post(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=RecommendationsResponse
)
async def get_recommendations(
        top_n: Annotated[int, Query(ge=MIN_TOP_N, le=MAX_TOP_N)],
        applicant: Applicant,
        recommendation_system: FromDishka[RecommendationSystem]
) -> RecommendationsResponse:
    with ThreadPoolExecutor() as executor:
        recommendations = await executor.submit(recommendation_system.recommend, applicant, top_n)
    # recommendations = recommendation_system.recommend(applicant, top_n)
    return RecommendationsResponse(recommendations=recommendations)
