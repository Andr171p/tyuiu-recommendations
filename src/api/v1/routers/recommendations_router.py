from fastapi import APIRouter, status
from dishka.integrations.fastapi import FromDishka

from src.core.entities import Applicant, Recommendations
from src.core.use_cases import RecommendationsUseCase


recommendations_router = APIRouter(
    tags=["Recommendations"],
    prefix="/api/v1/recommendations"
)


@recommendations_router.post(
    path="/",
    response_model=Recommendations,
    status_code=status.HTTP_200_OK
)
async def get_recommendations(
        applicant: Applicant,
        recommendations_use_case: FromDishka[RecommendationsUseCase]
) -> Recommendations:
    recommendations = recommendations_use_case.recommend(applicant)
    return recommendations
