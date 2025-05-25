from typing import List, Optional

from sqlalchemy import select, asc
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from ..domain import Direction, EntranceExam, PassingPoint, ReadableDirection
from .models import DirectionOrm, EntranceExamOrm, PassingPointOrm


class DirectionRepository:
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None:
        self.session_factory = session_factory

    async def read(self, direction_id: int) -> Optional[ReadableDirection]:
        async with self.session_factory() as session:
            stmt = (
                select(DirectionOrm)
                .where(DirectionOrm.direction_id == direction_id)
                .options(
                    selectinload(DirectionOrm.entrance_exams),
                    selectinload(DirectionOrm.passing_points)
                )
            )
            result = await session.execute(stmt)
        direction = result.scalar_one_or_none()
        print(direction)
        return ReadableDirection.model_validate(direction) if direction else None

    async def list(self) -> List[Direction]:
        async with self.session_factory() as session:
            stmt = select(DirectionOrm)
            results = await session.execute(stmt)
        directions = results.scalars().all()
        return [Direction.model_validate(direction) for direction in directions]


class EntranceExamRepository:
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None:
        self.session_factory = session_factory

    async def read(self, direction_id: int) -> List[EntranceExam]:
        async with self.session_factory() as session:
            stmt = (
                select(EntranceExamOrm)
                .where(EntranceExamOrm.direction_id == direction_id)
            )
            results = await session.execute(stmt)
        entrance_exams = results.scalars().all()
        return [EntranceExam.model_validate(entrance_exam) for entrance_exam in entrance_exams]


class PassingPointRepository:
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None:
        self.session_factory = session_factory

    async def sort(self, direction_id: int) -> List[PassingPoint]:
        async with self.session_factory() as session:
            stmt = (
                select(PassingPointOrm)
                .where(PassingPointOrm.direction_id == direction_id)
                .order_by(asc(PassingPointOrm.year))
            )
            results = await session.execute(stmt)
        passing_points = results.scalars().all()
        return [PassingPoint.model_validate(passing_point) for passing_point in passing_points]
