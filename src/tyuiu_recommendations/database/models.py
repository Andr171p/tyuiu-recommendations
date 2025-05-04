from sqlalchemy import ForeignKey, Index, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class DirectionOrm(Base):
    __tablename__ = "directions"

    direction_id: Mapped[int] = mapped_column(nullable=False, unique=True)
    education_form: Mapped[str] = mapped_column(nullable=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    entrance_exams: Mapped[list["EntranceExamOrm"]] = relationship(back_populates="direction")
    passing_points: Mapped[list["PassingPointsOrm"]] = relationship(back_populates="direction")

    __table_args__ = (
        Index("direction_index", "direction_id")
    )


class EntranceExamOrm(Base):
    __tablename__ = "entrance_exams"

    priority: Mapped[int]
    name: Mapped[str] = mapped_column(nullable=False)
    min_points: Mapped[int]

    direction_id: Mapped[int] = mapped_column(
            ForeignKey("directions.direction_id"),
            unique=False,
            nullable=False,
        )

    direction: Mapped["DirectionOrm"] = relationship(
        argument="DirectionOrm",
        back_populates="entrance_exams"
    )


class PassingPointsOrm(Base):
    __tablename__ = "passing_points"

    year: Mapped[int] = mapped_column(nullable=False)
    points: Mapped[int] = mapped_column(nullable=False)

    direction_id: Mapped[int] = mapped_column(
        ForeignKey("directions.direction_id"),
        unique=False,
        nullable=False,
    )

    direction: Mapped["DirectionOrm"] = relationship(
        argument="DirectionOrm",
        back_populates="passing_points"
    )
