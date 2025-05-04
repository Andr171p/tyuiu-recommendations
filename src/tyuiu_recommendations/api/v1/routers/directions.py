from typing import Annotated

from fastapi import (
    APIRouter,
    status,
    Depends,
    HTTPException
)

from src.tyuiu_recommendations.database.repositories import (
    DirectionRepository,
    EntranceExamRepository,
    PassingPointsRepository
)
from src.tyuiu_recommendations.dependencies import (
    get_direction_repository,
    get_entrance_exam_repository,
    get_passing_points_repository
)
from src.tyuiu_recommendations.entities import Direction
from ..schemas import EntranceExamsResponse, PassingPointsHistoryResponse


directions_router = APIRouter(
    prefix="/api/v1/directions",
    tags=["Directions"]
)


@directions_router.get(
    path="/{direction_id}",
    status_code=status.HTTP_200_OK,
    response_model=Direction
)
async def get_direction(
        direction_id: int,
        direction_repository: Annotated[DirectionRepository, Depends(get_direction_repository)]
) -> Direction:
    direction = await direction_repository.read(direction_id)
    if not direction:
        raise HTTPException(status_code=404, detail="Direction not found")
    return direction


@directions_router.get(
    path="/entrance-exams/{direction_id}",
    status_code=status.HTTP_200_OK,
    response_model=EntranceExamsResponse
)
async def get_entrance_exams(
        direction_id: int,
        entrance_exam_repository: Annotated[
            EntranceExamRepository,
            Depends(get_entrance_exam_repository)
        ]
) -> EntranceExamsResponse:
    entrance_exams = await entrance_exam_repository.read(direction_id)
    return EntranceExamsResponse(entrance_exams=entrance_exams)


@directions_router.get(
    path="/passing-points/{direction_id}",
    status_code=status.HTTP_200_OK,
    response_model=PassingPointsHistoryResponse
)
async def get_passing_points_history(
        direction_id: int,
        passing_points_repository: Annotated[
            PassingPointsRepository,
            Depends(get_passing_points_repository)
        ]
) -> PassingPointsHistoryResponse:
    sorted_passing_points = await passing_points_repository.get_sorted(direction_id)
    return PassingPointsHistoryResponse(history=sorted_passing_points)
