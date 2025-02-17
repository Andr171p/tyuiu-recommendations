from typing import Literal

from pydantic import BaseModel


class Exam(BaseModel):
    subject: Literal[
        "russian",
        "social_science",
        "math",
        "physics",
        "chemistry",
        "history",
        "informatics"
    ]
    points: int
