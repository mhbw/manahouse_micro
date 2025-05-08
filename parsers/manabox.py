import csv
from typing import List
from models.card import CardEntry

def normalize_set_code(set_name: str) -> str:
    return set_name.lower().replace(" ", "")[:5]

def normalize_finish(value: str) -> str:
    return "foil" if "foil" in value.lower() else "nonfoil"

def normalize_condition(value: str) -> str:
    cond = value.strip().title()
    valid = ["Near Mint", "Light Play", "Moderate Play", "Heavy Play", "Damaged"]
    return cond if cond in valid else "Near Mint"

def parse_manabox_csv(file_path: str) -> List[CardEntry]:
    entries = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                entry = CardEntry(
                    name=row["Name"].strip(),
                    set_code=normalize_set_code(row["Set"]),
                    set_name=row["Set"].strip(),
                    collector_number=row["Collector Number"].strip(),
                    finish=normalize_finish(row.get("Finish", "nonfoil")),
                    condition=normalize_condition(row.get("Condition", "Near Mint")),
                    lang=row.get("Language", "en").lower(),
                    quantity=int(row.get("Amount", 1)),
                    source_fields=row
                )
                entries.append(entry)
            except Exception as e:
                print(f"[WARN] Skipped row: {e}")
    return entries
