from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base_model import BaseModel
from src.database.models.direction_relation_mixin import DirectionRelationMixin


class EntranceExamModel(DirectionRelationMixin, BaseModel):
    __tablename__ = "entrance_exams"

    _direction_back_populates = "entrance_exams"

    priority: Mapped[int]
    name: Mapped[str] = mapped_column(nullable=False)
    min_points: Mapped[int]

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(priority={self.priority}, "
            f"name={self.name}, "
            f"min_points={self.min_points})"
        )

    def __repr__(self) -> str:
        return str(self)
