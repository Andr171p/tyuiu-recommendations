import json
import asyncio
from pprint import pprint

from src.database.models import DirectionModel, EntranceExamModel
from src.database.crud import DirectionCRUD
from src.database.database_manager import DatabaseManager
from src.config import BASE_DIR, settings

JSON_PATH = BASE_DIR / "datasets" / "Структурированные_направления_подготовки_с_id.json"

with open(
    file=JSON_PATH,
    mode="r",
    encoding="utf-8"
) as file:
    directions_json = json.load(file)


async def main() -> None:
    crud = DirectionCRUD(DatabaseManager(settings.postgres.url))
    for direction_json in directions_json:
        exams = []
        for exam in direction_json["Вступительные испытания"]:
            exam_model = EntranceExamModel(
                priority=int(exam["Приоритет"]),
                name=exam["Наименование"],
                min_points=exam["Минимальный балл"]
            )
            exams.append(exam_model)
        direction_model = DirectionModel(
            direction_id=int(direction_json["id"]),
            education_form=direction_json["Форма обучения"],
            name=direction_json["Шифр и наименование направления"],
            entrance_exams=exams,
            description=direction_json["Описание направления подготовки/специальности"]
        )
        try:
            await crud.create(direction_model)
        except Exception as _ex:
            print(_ex)


# asyncio.run(main())
