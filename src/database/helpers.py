from sqlalchemy import text

from src.database.models import BaseModel
from src.database.database_manager import DatabaseManager


async def truncate_and_reset_id(manager: DatabaseManager, model: BaseModel) -> None:
    async with manager.session() as session:
        await session.execute(text(f"DELETE FROM {model.__tablename__};"))
        await session.execute(text(f"ALTER SEQUENCE {model.__tablename__}_id_seq RESTART WITH 1;"))
        await session.commit()
