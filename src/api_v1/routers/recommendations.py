from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.core.entities import Applicant


recommendations_router = APIRouter(
    tags=["Recommendations"],
    prefix="/api/v1/recommendations"
)


@recommendations_router.post(path="/", response_model=...)
async def get_recommendations(applicant: Applicant) -> JSONResponse:
    ...
