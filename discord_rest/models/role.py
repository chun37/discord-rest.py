from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Role:
    id: str
    name: str
    permissions: str
    position: int
    color: int
    hoist: bool
    managed: bool
    mentionable: bool
    icon: Optional[Any]  # TODO: 型不明のためドキュメント待ち
    unicode_emoji: Optional[Any]  # TODO: 型不明のためドキュメント待ち
