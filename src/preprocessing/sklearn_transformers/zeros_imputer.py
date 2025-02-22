from typing import TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from pandas import DataFrame

from sklearn.base import BaseEstimator, TransformerMixin


class ZerosImputer(BaseEstimator, TransformerMixin):
    def __init__(self, columns: Optional[List[str]] = None) -> None:
        self.columns = columns

    def fit(self) -> "ZeroImputer":
        return self

    def transform(self, dataframe: "DataFrame") -> "DataFrame":
        if self.columns is not None:
            dataframe[self.columns] = dataframe[self.columns].fillna(0)
        dataframe = dataframe.fillna(0)
        return dataframe
