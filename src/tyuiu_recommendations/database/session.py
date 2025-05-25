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
