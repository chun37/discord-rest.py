from dataclasses import dataclass
from typing import Optional, Any

from .emoji import Emoji
from .sticker import Sticker
from .role import Role
from .voice import VoiceState
from .user import User
from .channel import Channel
from .stage_instance import StageInstance
from .member import Member


@dataclass
class WelcomeScreenChannel:
    channel_id: str
    description: str
    emoji_id: Optional[str]
    emoji_name: Optional[str]


@dataclass
class WelcomeScreen:
    description: Optional[str]
    welcome_channels: list[WelcomeScreenChannel]


@dataclass
class Guild:
    id: str
    name: str
    icon: Optional[str]
    icon_hash: Optional[str]
    splash: Optional[str]
    discovery_splash: Optional[str]
    owner: Optional[bool]
    owner_id: str
    permissions: Optional[str]
    region: Optional[str]
    afk_channel_id: Optional[str]
    afk_timeout: int
    widget_enabled: Optional[bool]
    widget_channel_id: Optional[str]
    verification_level: int
    default_message_notifications: int
    explicit_content_filter: int
    roles: list[Role]
    emojis: list[Emoji]
    features: list[str]
    mfa_level: int
    application_id: Optional[str]
    system_channel_id: Optional[str]
    system_channel_flags: int
    rules_channel_id: Optional[str]
    joined_at: Optional[str]
    large: Optional[bool]
    unavailable: Optional[bool]
    member_count: Optional[int]
    voice_states: Optional[list[VoiceState]]
    members: Optional[list[Member]]
    channels: Optional[list[Channel]]
    threads: Optional[list[Channel]]
    presences: Optional[list[Any]]
    max_presences: Optional[int]
    max_members: Optional[int]
    vanity_url_code: Optional[str]
    description: Optional[str]
    banner: Optional[str]
    premium_tier: int
    premium_subscription_count: Optional[int]
    preferred_locale: str
    public_updates_channel_id: Optional[str]
    max_video_channel_users: Optional[int]
    approximate_member_count: Optional[int]
    approximate_presence_count: Optional[int]
    welcome_screen: Optional[WelcomeScreen]
    nsfw_level: int
    stage_instances: Optional[list[StageInstance]]
    stickers: Optional[list[Sticker]]

    nsfw: bool  # undocumented
