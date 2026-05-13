# Struktura XLSX souborů pro Opening-hours

Tento dokument popisuje očekávanou strukturu Excel souborů pro skripty v repozitáři `X-Limited/Opening-hours`.

## Varianta: 7 řádků = 1 zákazník

Každý zákazník je reprezentovaný blokem 7 řádků:

1. Pondělí
2. Úterý
3. Středa
4. Čtvrtek
5. Pátek
6. Sobota
7. Neděle

## Vstupní sloupce

| Sloupec | Název | Popis |
|---|---|---|
| B | Název zákazníka | Název firmy pro Google Places lookup |
| C | Adresa | Ulice a číslo |
| D | PSČ | Poštovní směrovací číslo |
| E | Město | Obec / město |

## Výstupní sloupce

### Opening hours

| Sloupec | Význam |
|---|---|
| G | Otevřeno od – první interval |
| H | Otevřeno do – první interval |
| I | Otevřeno od – druhý interval |
| J | Otevřeno do – druhý interval |

## Google metadata

Tyto hodnoty se zapisují pouze do prvního řádku každého 7-bloku.

| Sloupec | Význam |
|---|---|
| AF | Google Place ID |
| AG | Google název |
| AH | Google adresa |
| AI | Latitude |
| AJ | Longitude |

## Barevné značení

| Barva | Význam |
|---|---|
| Zelená | Údaj úspěšně nalezen |
| Červená | Údaj chybí / nenalezen |

## Logika mapování dnů

Google Places používá:

| Google day index | Den |
|---|---|
| 1 | Pondělí |
| 2 | Úterý |
| 3 | Středa |
| 4 | Čtvrtek |
| 5 | Pátek |
| 6 | Sobota |
| 0 | Neděle |

## Doporučený skript

```text
scripts/google_opening_hours_7radku_v7_all_in_one.py
```

## API požadavky

Google Places API vyžaduje:

- Google Cloud projekt
- aktivní billing
- API key

Klíč se do GitHubu nikdy neukládá.

Používej:

```python
API_KEY = "SEM_VLOZ_GOOGLE_API_KEY"
```
