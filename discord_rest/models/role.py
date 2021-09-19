from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Tag:
    bot_id: Optional[str]
    integration_id: Optional[str]
    premium_subscriber: Optional[None]


@dataclass
class Role:
    id: str
    name: str
    color: int
    hoist: bool
    position: int
    permissions: str
    managed: bool
    mentionable: bool
    tags: Optional[Tag]

    icon: Optional[Any]  # TODO: 型不明のためドキュメント待ち
    unicode_emoji: Optional[Any]  # TODO: 型不明のためドキュメント待ち
