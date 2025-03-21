from pydantic import BaseModel


class PassingPoints(BaseModel):
    year: int
    points: int
    
    class Config:
        from_attributes = True
