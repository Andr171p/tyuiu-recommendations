from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from pathlib import Path

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


FEATURES = [
    "Пол",
    "Ср. балл док-та об образовании",
    "Сумма баллов",
    "Обществознание",
    "Математика",
    "Информатика",
    "Русский язык",
    "Физика",
    "Химия",
    "История"
]


class RecommendationSystem:
    def __init__(self, dataset_path: Union[str, "Path"]) -> None:
        self._df = pd.read_csv(dataset_path)

    def recommend(self, applicant_df: pd.DataFrame, top_n: int = 5) -> pd.DataFrame:
        combined_df = pd.concat([self._df[FEATURES], applicant_df], ignore_index=True)
        applicant_index = len(self._df)
        cosine_similarity_matrix = cosine_similarity(combined_df)
        similar_applicants_indices = cosine_similarity_matrix[applicant_index].argsort()[::-1][1:]
        recommendations = self._df.iloc[similar_applicants_indices][["Направление подготовки", "ID"]]
        recommendations = recommendations.drop_duplicates(subset=["Направление подготовки"])
        return recommendations.head(top_n)
