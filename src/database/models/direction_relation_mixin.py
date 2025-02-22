from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.database.models.direction_model import DirectionModel

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    declared_attr,
    relationship
)


class DirectionRelationMixin:
    _direction_id_nullable: bool = False
    _direction_id_unique: bool = False
    _direction_back_populates: Optional[str] = None

    @declared_attr
    def direction_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("directions.direction_id"),
            unique=cls._direction_id_unique,
            nullable=cls._direction_id_nullable,
        )

    @declared_attr
    def direction(cls) -> Mapped["DirectionModel"]:
        return relationship(
            argument="DirectionModel",
            back_populates=cls._direction_back_populates,
        )
