from typing import List, Union
from pathlib import Path

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from .constants import FEATURES
from .entities import Applicant, RecommendedDirection


class RecommendationSystem:
    def __init__(self, csv_path: Union[Path, str]) -> None:
        self._df = pd.read_csv(csv_path)

    def recommend(self, applicant: Applicant, top_n: int) -> List[RecommendedDirection]:
        applicant_df = applicant.to_df()
        combined_df = pd.concat([self._df[FEATURES], applicant_df], ignore_index=True)
        applicant_index = len(self._df)
        cosine_similarity_matrix = cosine_similarity(combined_df)
        similar_applicants_indices = cosine_similarity_matrix[applicant_index].argsort()[::-1][1:]
        recommendations = self._df.iloc[similar_applicants_indices][["Направление подготовки", "ID"]]
        recommendations = recommendations.drop_duplicates(subset=["Направление подготовки"])
        recommendations = recommendations.head(top_n)
        return [
            RecommendedDirection(direction_id=row["ID"], name=row["Направление подготовки"])
            for _, row in recommendations.iterrows()
        ]
