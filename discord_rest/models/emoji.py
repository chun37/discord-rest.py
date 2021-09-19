from dataclasses import dataclass
from typing import Optional

from .user import User


@dataclass(frozen=True)
class Emoji:
    id: str
    name: str
    roles: Optional[list[str]]
    user: Optional[User]
    require_colons: Optional[bool]
    managed: Optional[bool]
    animated: Optional[bool]
    available: Optional[bool]
