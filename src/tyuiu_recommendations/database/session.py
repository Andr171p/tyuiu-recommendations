from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)

from src.tyuiu_recommendations.settings import PostgresSettings


def create_sessionmaker(pg_settings: PostgresSettings) -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(url=pg_settings.sqlalchemy_url)
    return async_sessionmaker(
        engine,
        class_=AsyncSession,
        autoflush=False,
        expire_on_commit=False
    )


sessionmaker = create_sessionmaker(PostgresSettings())

from src.tyuiu_recommendations.database.repositories import DirectionRepository

repository = DirectionRepository(sessionmaker)

import asyncio


async def main() -> None:
    direction = await repository.read(8)
    print(direction)


asyncio.run(main())
