from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from src.api.dependencies import get_points_use_case
from src.core.use_cases import PointsUseCase
from src.core.entities import PointsHistory


points_router = APIRouter(
    prefix="/api/v1/points",
    tags=["Points"]
)


@points_router.get(path="/{direction_id}/", response_model=PointsHistory)
async def get_points_history_by_direction_id(
        direction_id: int,
        points_use_case: Annotated[
            PointsUseCase,
            Depends(get_points_use_case)
        ]
) -> JSONResponse:
    points_history = await points_use_case.get_by_direction_id(direction_id)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=points_history.model_dump()
    )
