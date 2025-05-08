from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

class CardPrice(BaseModel):
    scryfall_id: str
    source: Literal["scryfall", "tcgplayer", "cardkingdom"]
    channel: Optional[Literal["market", "direct", "retail"]] = "market"
    finish: Literal["nonfoil", "foil", "etched", "glossy"]
    condition: Literal["Near Mint", "Light Play", "Moderate Play", "Heavy Play", "Damaged"]
    currency: Literal["USD", "EUR", "TIX"]
    price: Optional[float]
    last_updated: datetime = Field(default_factory=datetime.utcnow)
