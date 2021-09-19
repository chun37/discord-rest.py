from dataclasses import dataclass
from typing import Optional


@dataclass
class Sticker:
    id: str
    name: str
    tags: str
    type: int
    format_type: int
    description: Optional[str]
    asset: str
    available: bool
    guild_id: str
