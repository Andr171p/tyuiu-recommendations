from typing import List

from src.repository.database.database_repository import DatabaseRepository
from src.services.database.models import PointsModel
from src.services.database.crud import PointsCRUD
from src.core.entities import Points


class PointsRepository(DatabaseRepository):
    def __init__(self, crud: PointsCRUD) -> None:
        self._crud = crud
        
    async def get_all(self) -> List[Points] | None:
        points = await self._crud.read_all()
        ...