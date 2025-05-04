from typing import List

from sqlalchemy import select, asc
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from ..entities import Direction, EntranceExam, PassingPoints
from .models import DirectionOrm, EntranceExamOrm, PassingPointsOrm



class DirectionRepository:
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None:
        self._session_factory = session_factory

    async def read(self, direction_id: int) -> Direction:
        async with self._session_factory() as session:
            stmt = (
                select(DirectionOrm)
                .where(DirectionOrm.direction_id == direction_id)
            )
            direction = await session.execute(stmt)
        return Direction.model_validate(direction.scalar_one())

    async def list(self) -> List[Direction]:
        async with self._session_factory() as session:
            stmt = select(DirectionOrm)
            directions = await session.execute(stmt)
        return [Direction.model_validate(direction) for direction in directions.scalars().all()]


class EntranceExamRepository:
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None:
        self._session_factory = session_factory

    async def read(self, direction_id: int) -> List[EntranceExam]:
        async with self._session_factory() as session:
            stmt = (
                select(EntranceExamOrm)
                .where(EntranceExamOrm.direction_id == direction_id)
            )
            entrance_exams = await session.execute(stmt)
        return [
            EntranceExam.model_validate(entrance_exam)
            for entrance_exam in entrance_exams.scalars().all()
        ]

    async def list(self) -> List[EntranceExam]:
        async with self._session_factory() as session:
            stmt = select(EntranceExamOrm)
            entrance_exams = await session.execute(stmt)
        return [
            EntranceExam.model_validate(entrance_exam)
            for entrance_exam in entrance_exams.scalars().all()
        ]


class PassingPointsRepository:
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None:
        self._session_factory = session_factory

    async def get_sorted(self, direction_id: int) -> List[PassingPoints]:
        async with self._session_factory() as session:
            stmt = (
                select(PassingPointsOrm)
                .where(PassingPointsOrm.direction_id == direction_id)
                .order_by(asc(PassingPointsOrm.year))
            )
            passing_points = await session.execute(stmt)
        return [
            PassingPoints.model_validate(passing_points)
            for passing_points in passing_points.scalars().all()
        ]

    async def list(self) -> List[PassingPoints]:
        async with self._session_factory() as session:
            stmt = select(PassingPointsOrm)
            passing_points = await session.execute(stmt)
        return [
            PassingPoints.model_validate(passing_points)
            for passing_points in passing_points.scalars().all()
        ]
