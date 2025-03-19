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

    def recommend(self, user_df: pd.DataFrame) -> pd.DataFrame:
        combined_df = pd.concat([self._df[FEATURES], user_df], ignore_index=True)
        user_index = len(self._df)
        cosine_similarity_matrix = cosine_similarity(combined_df)
        similar_users_indices = cosine_similarity_matrix[user_index].argsort()[::-1][1:]
        similar_users = combined_df.iloc[similar_users_indices]
        recommendations = similar_users.iloc[similar_users_indices][["Направление подготовки", "ID"]]
        return recommendations
