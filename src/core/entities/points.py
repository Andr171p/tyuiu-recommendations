from pydantic import BaseModel


class Points(BaseModel):
    year: int
    points: int
    
    class Config:
        from_attributes = True
