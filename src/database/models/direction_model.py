from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.services.database.models.points_model import PointsModel

from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.services.database.models.base_model import BaseModel


class DirectionModel(BaseModel):
    __tablename__ = 'directions'

    direction_id: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    points: Mapped[list["PointsModel"]] = relationship(back_populates="direction")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(direction_id={self.direction_id}, name={self.name}, description={self.description})"

    def __repr__(self) -> str:
        return str(self)
