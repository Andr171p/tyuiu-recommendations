from typing import Union

from pathlib import Path

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from .constants import FEATURES
from .domain import Applicant, Recommendation


class RecommendationSystem:
    def __init__(self, csv_path: Union[Path, str]) -> None:
        self.df = pd.read_csv(csv_path)

    def recommend(self, applicant: Applicant, top_n: int) -> list[Recommendation]:
        applicant_df = applicant.to_df()
        combined_df = pd.concat([self.df[FEATURES], applicant_df], ignore_index=True)
        applicant_index = len(self.df)
        cosine_similarity_matrix = cosine_similarity(combined_df)
        similar_applicants_indices = cosine_similarity_matrix[applicant_index].argsort()[::-1][1:]
        recommendations = self.df.iloc[similar_applicants_indices][["Направление подготовки", "ID"]]
        recommendations = recommendations.drop_duplicates(subset=["Направление подготовки"])
        recommendations = recommendations.head(top_n)
        return [
            Recommendation(direction_id=row["ID"], name=row["Направление подготовки"])
            for _, row in recommendations.iterrows()
        ]

    def _filter_by_subjects(self, subjects: list[str]) -> pd.DataFrame:
        mask = (self.df[subjects] > 0).all(axis=1)
        return self.df[mask].copy()
