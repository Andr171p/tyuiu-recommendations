from fastapi import APIRouter, status
from dishka.integrations.fastapi import FromDishka

from src.core.use_cases import PointsUseCase
from src.core.entities import PointsHistory


points_router = APIRouter(
    prefix="/api/v1/points",
    tags=["Points"]
)


@points_router.get(
    path="/{direction_id}/",
    response_model=PointsHistory,
    status_code=status.HTTP_200_OK
)
async def get_points_history_by_direction_id(
        direction_id: int,
        points_use_case: FromDishka[PointsUseCase]
) -> PointsHistory:
    points_history = await points_use_case.get_by_direction_id(direction_id)
    return points_history
