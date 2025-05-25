from sqlalchemy import Index, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class DirectionOrm(Base):
    __tablename__ = "directions"

    direction_id: Mapped[int] = mapped_column(unique=True, nullable=True)
    name: Mapped[str] = mapped_column(nullable=False)
    education_form: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    entrance_exams: Mapped[list["EntranceExamOrm"]] = relationship(back_populates="direction")
    passing_points: Mapped[list["PassingPointOrm"]] = relationship(back_populates="direction")

    __table_args__ = (
        Index("direction_index", "id"),
    )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(direction_id={self.direction_id}, "
            f"name={self.name}, "
            f"education_form={self.education_form}"
            f")"
        )

    def __repr__(self) -> str:
        return str(self)


class EntranceExamOrm(Base):
    __tablename__ = "entrance_exams"

    direction_id: Mapped[int] = mapped_column(
        ForeignKey("directions.direction_id"),
        unique=False,
        nullable=False,
    )
    name: Mapped[str] = mapped_column(nullable=False)
    priority: Mapped[int]
    min_points: Mapped[int]

    direction: Mapped["DirectionOrm"] = relationship(
        argument="DirectionOrm",
        back_populates="entrance_exams"
    )


class PassingPointOrm(Base):
    __tablename__ = "passing_points"

    direction_id: Mapped[int] = mapped_column(
        ForeignKey("directions.direction_id"),
        unique=False,
        nullable=False,
    )
    year: Mapped[int] = mapped_column(nullable=False)
    points: Mapped[int] = mapped_column(nullable=False)

    direction: Mapped["DirectionOrm"] = relationship(
        argument="DirectionOrm",
        back_populates="passing_points"
    )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(direction_id={self.direction_id}, "
            f"year={self.year}, "
            f"points={self.points}"
            f")"
        )

    def __repr__(self) -> str:
        return str(self)
