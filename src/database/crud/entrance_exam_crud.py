from typing import Sequence

from sqlalchemy import select, asc

from src.database.crud.base_crud import BaseCRUD
from src.database.models import EntranceExamModel
from src.database.database_manager import DatabaseManager


class EntranceExamCRUD(BaseCRUD):
    def __init__(self, manager: DatabaseManager) -> None:
        self._manager = manager

    async def create(self, entrance_exam: EntranceExamModel) -> int:
        async with self._manager.session() as session:
            session.add(entrance_exam)
            id = entrance_exam.id
            await session.commit()
        return id

    async def read_by_direction_id(self, direction_id: int) -> Sequence[EntranceExamModel]:
        async with self._manager.session() as session:
            stmt = (
                select(EntranceExamModel)
                .where(EntranceExamModel.direction_id == direction_id)
                .order_by(asc(EntranceExamModel.priority))
            )
            entrance_exam = await session.execute(stmt)
        return entrance_exam.scalars().all()

    async def read_all(self) -> Sequence[EntranceExamModel]:
        async with self._manager.session() as session:
            stmt = select(EntranceExamModel)
            entrance_exams = await session.execute(stmt)
        return entrance_exams.scalars().all()
