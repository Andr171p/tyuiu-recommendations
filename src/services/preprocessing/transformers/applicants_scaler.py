from pathlib import Path
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from numpy import ndarray
    from pandas import DataFrame
    from sklearn.preprocessing import StandardScaler

from joblib import load
from sklearn.base import BaseEstimator, TransformerMixin


class ApplicantsScaler(BaseEstimator, TransformerMixin):
    def __init__(self,  path: Union[Path, str]) -> None:
        self._scaler: "StandardScaler" = load(path)

    def transform(
            self,
            dataframe: "DataFrame",
    ) -> "ndarray[float]":
        scaled_array = self._scaler.transform(dataframe)
        return scaled_array
