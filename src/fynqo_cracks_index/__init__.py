"""
fynqo-cracks-index — Python client voor de Cracks Index dataset.

De Cracks Index meet financiële kwetsbaarheid van Nederlandse huishoudens
op gemeente- en wijkniveau. De brondata staat op HuggingFace:

    https://huggingface.co/datasets/jan12456/cracks-index

Dit pakket is een dunne wrapper rond `datasets.load_dataset()` met een
pandas-vriendelijke API voor analisten.

Maintained by Fynqo — https://fynqo.app/cracks-index
"""

from __future__ import annotations

from .client import CracksIndex, load, __all__ as _client_all
from .version import __version__

__all__ = ["CracksIndex", "load", "__version__", *_client_all]
