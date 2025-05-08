from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime

class CardEntry(BaseModel):
    scryfall_id: Optional[str] = None
    name: str
    collector_number: str
    set_code: str
    set_name: Optional[str] = None
    lang: str = "en"
    finish: str
    frame_effects: Optional[List[str]] = []
    condition: str
    quantity: int = Field(ge=0)
    tcgplayer_id: Optional[int] = None
    mana_house_tags: Optional[List[str]] = []
    source_fields: Optional[Dict[str, str]] = None
    added_at: datetime = Field(default_factory=datetime.utcnow)
