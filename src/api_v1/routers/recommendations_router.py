from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from src.core.entities import Applicant, Recommendations
from src.core.use_cases import RecommendationsUseCase
from src.api_v1.dependencies import get_recommendations_use_case


recommendations_router = APIRouter(
    tags=["Recommendations"],
    prefix="/api/v1/recommendations"
)


@recommendations_router.post(path="/", response_model=Recommendations)
async def get_recommendations(
        applicant: Applicant,
        recommendations_use_case: Annotated[
            RecommendationsUseCase,
            Depends(get_recommendations_use_case)
        ]
) -> JSONResponse:
    recommendations = recommendations_use_case.recommend(applicant)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=recommendations.model_dump()
    )
