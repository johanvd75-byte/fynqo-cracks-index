"""
Client for the Cracks Index dataset on HuggingFace.

The default dataset id is `jan12456/cracks-index`. You can override it via
the `dataset_id` argument or the `CRACKS_INDEX_DATASET` env var.

Quick start:

    from fynqo_cracks_index import load
    df = load(split="train").to_pandas()
    print(df.head())

Or with the class API:

    from fynqo_cracks_index import CracksIndex
    idx = CracksIndex()
    df = idx.dataframe()
    municipality = idx.by_municipality("Amsterdam")
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Iterable, Optional

if TYPE_CHECKING:  # pragma: no cover
    import pandas as pd
    from datasets import Dataset, DatasetDict

DEFAULT_DATASET_ID = "jan12456/cracks-index"

__all__ = ["DEFAULT_DATASET_ID"]


def load(
    dataset_id: Optional[str] = None,
    split: str = "train",
    **kwargs: Any,
) -> "Dataset":
    """
    Load the Cracks Index dataset directly via 🤗 datasets.

    Thin convenience wrapper that defers the heavy import so the package
    stays importable in environments without `datasets` installed.

    Parameters
    ----------
    dataset_id : str, optional
        HuggingFace dataset id. Defaults to env `CRACKS_INDEX_DATASET` or
        `jan12456/cracks-index`.
    split : str
        Which split to load. Defaults to "train".
    **kwargs : Any
        Forwarded to `datasets.load_dataset`.
    """
    from datasets import load_dataset  # local import: heavy

    target = dataset_id or os.environ.get("CRACKS_INDEX_DATASET", DEFAULT_DATASET_ID)
    return load_dataset(target, split=split, **kwargs)


@dataclass
class CracksIndex:
    """
    Pandas-friendly accessor for the Cracks Index dataset.

    Loads lazily on first access. Caches the DataFrame for the lifetime
    of the instance.
    """

    dataset_id: str = DEFAULT_DATASET_ID
    split: str = "train"
    _df: Optional["pd.DataFrame"] = field(default=None, repr=False, init=False)

    def dataframe(self, refresh: bool = False) -> "pd.DataFrame":
        """Return the dataset as a pandas DataFrame."""
        if self._df is None or refresh:
            ds = load(self.dataset_id, split=self.split)
            self._df = ds.to_pandas()
        return self._df

    # ----- convenience filters -------------------------------------------------

    def columns(self) -> list[str]:
        return list(self.dataframe().columns)

    def by_municipality(self, name: str, column: str = "gemeente") -> "pd.DataFrame":
        """
        Filter rows by municipality (case-insensitive exact match).
        Column name defaults to 'gemeente'; override if the schema differs.
        """
        df = self.dataframe()
        if column not in df.columns:
            raise KeyError(
                f"Column {column!r} not in dataset. Available: {list(df.columns)}"
            )
        return df[df[column].astype(str).str.casefold() == name.casefold()].copy()

    def top(self, n: int = 10, by: str = "cracks_index") -> "pd.DataFrame":
        """Return the top-N rows by a numeric column (defaults to 'cracks_index')."""
        df = self.dataframe()
        if by not in df.columns:
            raise KeyError(
                f"Column {by!r} not in dataset. Available: {list(df.columns)}"
            )
        return df.nlargest(n, by).copy()

    def iter_records(self) -> Iterable[dict[str, Any]]:
        """Yield rows as plain dicts (useful for streaming pipelines)."""
        for record in self.dataframe().to_dict(orient="records"):
            yield record
