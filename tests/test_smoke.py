"""
Smoke tests — do not hit the network.

For real integration tests, set CRACKS_INDEX_RUN_NETWORK=1 in your CI env.
"""

import os
import pytest

import fynqo_cracks_index
from fynqo_cracks_index import CracksIndex, DEFAULT_DATASET_ID, __version__


def test_version_string():
    assert isinstance(__version__, str)
    assert len(__version__.split(".")) >= 2


def test_default_dataset_id():
    assert DEFAULT_DATASET_ID == "jan12456/cracks-index"


def test_class_initialises_lazily():
    idx = CracksIndex()
    assert idx.dataset_id == DEFAULT_DATASET_ID
    assert idx._df is None  # nothing loaded yet


@pytest.mark.skipif(
    os.environ.get("CRACKS_INDEX_RUN_NETWORK") != "1",
    reason="set CRACKS_INDEX_RUN_NETWORK=1 to run network test",
)
def test_load_real_dataset():
    df = CracksIndex().dataframe()
    assert len(df.columns) > 0
    assert len(df) > 0
