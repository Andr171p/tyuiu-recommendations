import pandas as pd

from src.core.entities import Recommendations, RecommendedDirection


class RecommendationsMapper:
    @staticmethod
    def from_df(df: pd.DataFrame) -> Recommendations:
        directions = [
            RecommendedDirection(direction_id=row["ID"], name=row["Направление подготовки"])
            for _, row in df.iterrows()
        ]
        return Recommendations(directions=directions)
