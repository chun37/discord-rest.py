from dataclasses import dataclass
from typing import Optional

from .emoji import Emoji
from .sticker import Sticker
from .role import Role


@dataclass
class Guild:
    id: str
    name: str
    icon: Optional[str]
    description: Optional[str]
    splash: Optional[str]
    discovery_splash: Optional[str]
    features: list[str]
    emojis: list[Emoji]
    stickers: list[Sticker]
    banner: Optional[str]
    owner_id: str
    application_id: Optional[str]
    region: Optional[str]
    afk_channel_id: Optional[str]
    afk_timeout: int
    system_channel_id: Optional[str]
    widget_enabled: bool
    widget_channel_id: Optional[str]
    verification_level: int
    roles: list[Role]
    default_message_notifications: int
    mfa_level: int
    explicit_content_filter: int
    max_presences: Optional[int]
    max_members: int
    max_video_channel_users: int
    vanity_url_code: Optional[str]
    premium_tier: int
    premium_subscription_count: int
    system_channel_flags: int
    preferred_locale: str
    rules_channel_id: Optional[str]
    public_updates_channel_id: Optional[str]
    nsfw: bool  # undocumented
    nsfw_level: int
    approximate_member_count: Optional[int]
    approximate_presence_count: Optional[int]
