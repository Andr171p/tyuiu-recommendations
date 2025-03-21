from typing import Literal

from pydantic import BaseModel


class Direction(BaseModel):
    direction_id: int
    education_form: Literal["ОФО", "ЗФО"]
    name: str
    description: str
    
    class Config:
        from_attributes = True
