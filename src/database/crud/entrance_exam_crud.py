from typing import Sequence, Union

from sqlalchemy import select

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

    async def read_by_direction_id(self, direction_id: int) -> Union[EntranceExamModel, None]:
        async with self._manager.session() as session:
            stmt = (
                select(EntranceExamModel)
                .where(EntranceExamModel.direction_id == direction_id)
            )
            entrance_exam = await session.execute(stmt)
        return entrance_exam.scalar_one_or_none()

    async def read_all(self) -> Sequence[EntranceExamModel]:
        async with self._manager.session() as session:
            stmt = select(EntranceExamModel)
            entrance_exams = await session.execute(stmt)
        return entrance_exams.scalars().all()
