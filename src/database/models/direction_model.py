from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.database.models.entrance_exam_model import EntranceExamModel
    from src.database.models.passing_points_model import PassingPointsModel

from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base_model import BaseModel


class DirectionModel(BaseModel):
    __tablename__ = "directions"

    direction_id: Mapped[int] = mapped_column(nullable=False, unique=True)
    education_form: Mapped[str] = mapped_column(nullable=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    entrance_exams: Mapped[list["EntranceExamModel"]] = relationship(back_populates="direction")
    passing_points: Mapped[list["PassingPointsModel"]] = relationship(back_populates="direction")

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(direction_id={self.direction_id},"
            f"education_form={self.education_form},"
            f"name={self.name}, "
            f"description={self.description})"
        )

    def __repr__(self) -> str:
        return str(self)
