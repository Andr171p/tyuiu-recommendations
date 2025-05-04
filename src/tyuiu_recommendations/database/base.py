from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


