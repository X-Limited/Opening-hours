# Google Places Opening Hours Automation

[![CI](https://github.com/X-Limited/Opening-hours/actions/workflows/ci.yml/badge.svg)](https://github.com/X-Limited/Opening-hours/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

Projekt pro automatizované dohledávání otevíracích dob firem pomocí Google Places API.

## Funkce

- dohledání Google Place ID,
- opening hours,
- geolokace Latitude / Longitude,
- export do Excelu,
- barevné validace,
- podpora 7 řádků = 1 zákazník,
- dvojité intervaly otevírací doby,
- bulk processing.

## Technologie

- Python
- Google Places API
- requests
- openpyxl

## Doporučená verze

```text
scripts/google_opening_hours_7radku_v7_all_in_one.py
```

## Instalace

```bash
pip install -r requirements.txt
```

## Bezpečnost

Google API klíč není ukládán do repozitáře.

Používej:

```python
API_KEY = "SEM_VLOZ_GOOGLE_API_KEY"
```

## License

[MIT](LICENSE) © 2026 X-Limited
