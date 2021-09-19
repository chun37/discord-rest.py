from dataclasses import dataclass
from typing import Optional

from .user import User


@dataclass
class Member:
    user: Optional[User]
    nick: Optional[str]
    roles: list[str]
    joined_at: str
    premium_since: Optional[str]
    deaf: bool
    mute: bool
    pending: Optional[bool]
    permissions: Optional[str]
