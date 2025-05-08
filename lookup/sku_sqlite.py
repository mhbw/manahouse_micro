import sqlite3
from models.card import CardEntry
from typing import Optional

def resolve_sku_from_db(entry: CardEntry, db_path="data/tcgplayer_skus.db") -> Optional[int]:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        SELECT sku_id FROM sku_map
        WHERE product_id = ?
        AND finish = ?
        AND condition = ?
        AND language = ?
        LIMIT 1
    """, (entry.tcgplayer_id, entry.finish, entry.condition, entry.lang))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None
