from pydantic import BaseModel


class Direction(BaseModel):
    name: str
    description: str
    link: str
