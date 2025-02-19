from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from src.core.entities import Applicant, Recommendations
from src.interations import RecommendationsInteration
from src.api_v1.dependencies import get_recommendations_interaction


recommendations_router = APIRouter(
    tags=["Recommendations"],
    prefix="/api/v1/recommendations"
)


@recommendations_router.post(path="/", response_model=Recommendations)
async def get_recommendations(
        applicant: Applicant,
        recommendations_interaction: Annotated[
            RecommendationsInteration,
            Depends(get_recommendations_interaction)
        ]
) -> JSONResponse:
    print(type(recommendations_interaction))
    recommendations = recommendations_interaction.get_recommendations(applicant)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=recommendations.model_dump()
    )
