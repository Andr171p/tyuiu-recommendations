from fastapi import APIRouter, status, HTTPException

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.tyuiu_recommendations.database.repositories import (
    DirectionRepository,
    EntranceExamRepository,
    PassingPointRepository
)
from src.tyuiu_recommendations.domain import ReadableDirection
from ..schemas import EntranceExamsResponse, PassingPointsResponse


directions_router = APIRouter(
    prefix="/api/v1/directions",
    tags=["Directions"],
    route_class=DishkaRoute
)


@directions_router.get(
    path="/{direction_id}",
    status_code=status.HTTP_200_OK,
    response_model=ReadableDirection
)
async def get_direction(
        direction_id: int,
        direction_repository: FromDishka[DirectionRepository]
) -> ReadableDirection:
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
        entrance_exam_repository: FromDishka[EntranceExamRepository]
) -> EntranceExamsResponse:
    entrance_exams = await entrance_exam_repository.read(direction_id)
    if not entrance_exams:
        raise HTTPException(status_code=404, detail="Entrance exams not found")
    return EntranceExamsResponse(entrance_exams=entrance_exams)


@directions_router.get(
    path="/passing-points/{direction_id}",
    status_code=status.HTTP_200_OK,
    response_model=PassingPointsResponse
)
async def get_passing_points_history(
        direction_id: int,
        passing_point_repository: FromDishka[PassingPointRepository]
) -> PassingPointsResponse:
    sorted_passing_points = await passing_point_repository.sort(direction_id)
    return PassingPointsResponse(passing_points=sorted_passing_points)
