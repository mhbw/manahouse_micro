import csv
from models.card import CardEntry

def format_tcgplayer_condition(condition: str, finish: str) -> str:
    return f"{condition} Foil" if finish == "foil" else condition

def export_cards_to_tcgplayer_csv(cards, output_path):
    with open(output_path, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[
            "Product Name", "Set Name", "Condition", "Language", "Quantity", "TCGPlayer SKU"
        ])
        writer.writeheader()
        for card in cards:
            writer.writerow({
                "Product Name": card.name,
                "Set Name": card.set_name,
                "Condition": format_tcgplayer_condition(card.condition, card.finish),
                "Language": card.lang,
                "Quantity": card.quantity,
                "TCGPlayer SKU": card.source_fields.get("tcgplayer_sku", "")
            })

def export_cards_to_csv(cards, output_path):
    with open(output_path, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[
            "name", "set_code", "collector_number", "finish", "condition",
            "quantity", "scryfall_id", "tcgplayer_id", "price"
        ])
        writer.writeheader()
        for card in cards:
            writer.writerow({
                "name": card.name,
                "set_code": card.set_code,
                "collector_number": card.collector_number,
                "finish": card.finish,
                "condition": card.condition,
                "quantity": card.quantity,
                "scryfall_id": card.scryfall_id,
                "tcgplayer_id": card.tcgplayer_id,
                "price": card.source_fields.get("price", None),
            })
