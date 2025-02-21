from pydantic import BaseModel


class Direction(BaseModel):
    direction_id: int
    name: str
    description: str
    
    class Config:
        from_attributes = True
