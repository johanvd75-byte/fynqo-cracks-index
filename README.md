# fynqo-cracks-index

Python client voor de [**Cracks Index** dataset](https://huggingface.co/datasets/jan12456/cracks-index)
op HuggingFace — een dataset die financiële kwetsbaarheid van Nederlandse
huishoudens meet op gemeente- en wijkniveau.

Dit pakket is een dunne wrapper rond `datasets.load_dataset()` plus een
pandas-vriendelijke accessor voor analisten en onderzoekers.

## Install

```bash
pip install fynqo-cracks-index
```

## Quick start

```python
from fynqo_cracks_index import load, CracksIndex

# Functional API
df = load(split="train").to_pandas()

# Class API (with caching)
idx = CracksIndex()
df = idx.dataframe()

print(idx.columns())
print(idx.by_municipality("Amsterdam"))
print(idx.top(n=10, by="cracks_index"))
```

## Configuratie

- `CRACKS_INDEX_DATASET` (env) — override de dataset-id, handig voor
  forks of dev-mirrors.

## Citeren

Gebruik je deze data in onderzoek? Citeer de bron via de Zenodo-DOI:

- Dataset: <https://huggingface.co/datasets/jan12456/cracks-index>
- DOI: zie de Zenodo-record (CITATION op fynqo.app/cracks-index)

## Achtergrond

De Cracks Index is een open metingsmethode voor financiële stress in
Nederlandse huishoudens. Methodologie en updates:

- <https://fynqo.app/cracks-index>

## License

MIT — zie [LICENSE](./LICENSE). De dataset zelf valt onder de licentie
van de dataset-publisher op HuggingFace.

## About

Maintained by [Fynqo](https://fynqo.app) — schuldhulp, budgetcoaching
en financiële inzichten.

- Website: <https://fynqo.app>
- Contact: <info@fynqo.app>
- Source: <https://github.com/fynqo/fynqo-cracks-index>
