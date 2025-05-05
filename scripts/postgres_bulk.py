import json
import asyncio

import pandas as pd

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)

from src.tyuiu_recommendations.settings import BASE_DIR
from src.tyuiu_recommendations.settings import PostgresSettings
from src.tyuiu_recommendations.database.models import (
    DirectionOrm,
    EntranceExamOrm,
    PassingPointsOrm
)

JSON_PATH = BASE_DIR / "datasets" / "jsons" / "Структурированные_направления_подготовки_с_id.json"

DF_PATH = BASE_DIR / "notebooks" / "ТИУ_проходные_баллы_2014-2024.csv"


df = pd.read_csv(DF_PATH)

with open(file=JSON_PATH, encoding="utf-8") as file:
    directions_json = json.load(file)


async def main() -> None:
    engine = create_async_engine(url=PostgresSettings().sqlalchemy_url)
    sessionmaker = async_sessionmaker(
        engine,
        class_=AsyncSession,
        autoflush=False,
        expire_on_commit=False
    )
    async with sessionmaker() as session:
        for direction_json in directions_json:
            exams = []
            for exam in direction_json["Вступительные испытания"]:
                exam_orm = EntranceExamOrm(
                    priority=int(exam["Приоритет"]),
                    name=exam["Наименование"],
                    min_points=exam["Минимальный балл"]
                )
                exams.append(exam_orm)
            direction_orm = DirectionOrm(
                direction_id=int(direction_json["id"]),
                education_form=direction_json["Форма обучения"],
                name=direction_json["Шифр и наименование направления"],
                entrance_exams=exams,
                description=direction_json["Описание направления подготовки/специальности"]
            )
            try:
                session.add(direction_orm)
                await session.commit()
            except Exception as ex:
                print(ex)

    async with sessionmaker() as session:
        for _, row in df.iterrows():
            passing_points_orm = PassingPointsOrm(
                direction_id=row["ID"],
                year=row["Год"],
                points=row["Сумма баллов"]
            )
            try:
                session.add(passing_points_orm)
                await session.commit()
            except Exception as _ex:
                print(_ex)


if __name__ == "__main__":
    asyncio.run(main())
