from dataclasses import dataclass
from typing import Optional

from .user import User


@dataclass
class Sticker:
    id: str
    pack_id: Optional[str]
    name: str
    description: Optional[str]
    tags: str
    asset: str
    type: int
    format_type: int
    available: Optional[bool]
    guild_id: Optional[str]
    user: Optional[User]
    sort_value: Optional[int]