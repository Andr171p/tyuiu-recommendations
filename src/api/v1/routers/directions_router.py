from fastapi import APIRouter, status
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.core.use_cases import DirectionsUseCase
from src.core.entities import Direction, PassingPointsHistory, EntranceExamsSortByPriority


directions_router = APIRouter(
    prefix='/ap1/v1/directions',
    tags=['Directions'],
    route_class=DishkaRoute
)


@directions_router.get(
    path="/{direction_id}/",
    response_model=Direction,
    status_code=status.HTTP_200_OK
)
async def get_by_direction_id(
        direction_id: int,
        directions_use_case: FromDishka[DirectionsUseCase]
) -> Direction:
    direction = await directions_use_case.get_by_direction_id(direction_id)
    return direction


@directions_router.get(
    path="/entrance-exams/{direction_id}/",
    response_model=EntranceExamsSortByPriority,
    status_code=status.HTTP_200_OK
)
async def get_entrance_exams(
        direction_id: int,
        directions_use_case: FromDishka[DirectionsUseCase]
) -> EntranceExamsSortByPriority:
    entrance_exams = await directions_use_case.get_entrance_exams(direction_id)
    return entrance_exams


@directions_router.get(
    path="/passing-points/{direction_id}/",
    response_model=PassingPointsHistory,
    status_code=status.HTTP_200_OK
)
async def get_passing_points_history(
        direction_id: int,
        directions_use_case: FromDishka[DirectionsUseCase]
) -> PassingPointsHistory:
    passing_points_history = await directions_use_case.get_passing_points_history(direction_id)
    return passing_points_history
