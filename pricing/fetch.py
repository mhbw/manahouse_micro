import requests
from datetime import datetime
from models.price import CardPrice

CONDITION_ADJUSTMENT = {
    "Near Mint": 1.0,
    "Light Play": 0.9,
    "Moderate Play": 0.7,
    "Heavy Play": 0.5,
    "Damaged": 0.25
}

def fetch_price_from_scryfall(scryfall_id: str, finish: str, condition: str) -> CardPrice:
    url = f"https://api.scryfall.com/cards/{scryfall_id}"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    price_key = "usd_foil" if finish == "foil" else "usd"
    base_price = float(data.get("prices", {}).get(price_key) or 0.0)
    adjusted_price = round(base_price * CONDITION_ADJUSTMENT.get(condition, 1.0), 2)
    return CardPrice(
        scryfall_id=scryfall_id,
        source="scryfall",
        finish=finish,
        condition=condition,
        currency="USD",
        price=adjusted_price,
        last_updated=datetime.utcnow()
    )
