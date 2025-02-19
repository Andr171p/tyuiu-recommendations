from pathlib import Path
from typing import TYPE_CHECKING, Union, Optional

if TYPE_CHECKING:
    from pandas import DataFrame
    from sklearn.preprocessing import LabelEncoder

from joblib import load
from sklearn.base import BaseEstimator, TransformerMixin


class ForeignCitizenshipEncoder(BaseEstimator, TransformerMixin):
    def __init__(self,  path: Union[Path, str]) -> None:
        self.path = path
        self._encoder: "LabelEncoder" = load(self.path)

    def fit(
            self,
            dataframe: "DataFrame",
            y: Optional["DataFrame"] = None
    ) -> "ForeignCitizenshipEncoder":
        self._encoder.fit(dataframe)
        return self

    def transform(
            self,
            dataframe: "DataFrame",
            column: str = "foreign_citizenship"
    ) -> "DataFrame":
        dataframe[column] = self._encoder.transform(dataframe[column])
        return dataframe
