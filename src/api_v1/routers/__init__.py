__all__ = (
    "recommendations_router",
    "directions_router",
    "points_router"
)

from src.api_v1.routers.recommendations_router import recommendations_router
from src.api_v1.routers.directions_router import directions_router
from src.api_v1.routers.points_router import points_router
