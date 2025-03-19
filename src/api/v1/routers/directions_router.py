from fastapi import APIRouter, status
from dishka.integrations.fastapi import FromDishka

from src.core.entities import Direction
from src.core.use_cases import DirectionUseCase


directions_router = APIRouter(
    prefix='/ap1/v1/directions',
    tags=['Directions'],
)


@directions_router.get(
    path="/{direction_id}/",
    response_model=Direction,
    status_code=status.HTTP_200_OK
)
async def get_by_direction_id(
        direction_id: int,
        direction_use_case: FromDishka[DirectionUseCase]
) -> Direction:
    direction = await direction_use_case.get_by_direction_id(direction_id)
    return direction
