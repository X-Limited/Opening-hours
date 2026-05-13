# Google Places Opening Hours Automation

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
