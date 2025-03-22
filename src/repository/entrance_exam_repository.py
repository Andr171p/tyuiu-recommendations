from typing import List, Union

from src.core.entities import EntranceExam
from src.database.crud import EntranceExamCRUD
from src.database.models import EntranceExamModel
from src.repository.base_repository import BaseRepository


class EntranceExamRepository(BaseRepository):
    def __init__(self, crud: EntranceExamCRUD) -> None:
        self._crud = crud

    async def save(self, entrance_exam: EntranceExam) -> int:
        id = await self._crud.create(EntranceExamModel(**entrance_exam.model_dump()))
        return id

    async def get_by_direction_id(self, direction_id: int) -> List[Union[EntranceExam, None]]:
        entrance_exams = await self._crud.read_by_direction_id(direction_id)
        return [
            EntranceExam.model_validate(entrance_exam)
            for entrance_exam in entrance_exams
        ] if entrance_exams else []

    async def get_all(self) -> List[Union[EntranceExam, None]]:
        entrance_exams = await self._crud.read_all()
        return [
            EntranceExam.model_validate(entrance_exam)
            for entrance_exam in entrance_exams
        ] if entrance_exams else []
