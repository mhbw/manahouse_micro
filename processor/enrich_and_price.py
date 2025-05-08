from typing import List, Tuple
import time
from scryfall.enrich import enrich_card_with_scryfall
from pricing.fetch import fetch_price_from_scryfall
from lookup.sku_sqlite import resolve_sku_from_db
from models.card import CardEntry

def enrich_and_price_cards(cards: List[CardEntry], delay: float = 0.2, sku_db_path: str = "data/tcgplayer_skus.db") -> Tuple[List[CardEntry], List[CardEntry]]:
    enriched, failed = [], []
    for i, card in enumerate(cards):
        print(f"[{i+1}/{len(cards)}] Processing: {card.name} ({card.set_code}) #{card.collector_number}")
        try:
            enriched_card = enrich_card_with_scryfall(card)
            if enriched_card.scryfall_id:
                price = fetch_price_from_scryfall(enriched_card.scryfall_id, enriched_card.finish, enriched_card.condition)
                enriched_card.source_fields["price"] = price.price
                sku_id = resolve_sku_from_db(enriched_card, db_path=sku_db_path)
                if sku_id:
                    enriched_card.source_fields["tcgplayer_sku"] = sku_id
            else:
                failed.append(card)
                continue
            enriched.append(enriched_card)
        except Exception as e:
            print(f"[ERROR] {e}")
            failed.append(card)
        time.sleep(delay)
    return enriched, failed
