import requests
from models.card import CardEntry

def enrich_card_with_scryfall(entry: CardEntry) -> CardEntry:
    url = f"https://api.scryfall.com/cards/{entry.set_code}/{entry.collector_number}?lang={entry.lang}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"[WARN] Scryfall failed: {entry.name} ({entry.set_code}) #{entry.collector_number}")
        return entry
    data = response.json()
    entry.scryfall_id = data["id"]
    entry.name = data["name"]
    entry.set_name = data["set_name"]
    entry.tcgplayer_id = data.get("tcgplayer_id")
    entry.frame_effects = data.get("frame_effects", [])
    return entry
