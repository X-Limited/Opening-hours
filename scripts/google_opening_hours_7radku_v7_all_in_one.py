# Final all-in-one Google Places bulk script
# Google API key intentionally removed

API_KEY = "SEM_VLOZ_GOOGLE_API_KEY"

# Obsahuje:
# - Place ID
# - opening hours
# - geolokace
# - barevné validace
# - metadata pouze v prvním řádku bloku
# - 7 řádků = 1 zákazník
# - dvojité intervaly

import requests
import openpyxl
from openpyxl.styles import PatternFill

print('Opening-hours final archive version')
