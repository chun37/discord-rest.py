from dataclasses import dataclass
from typing import Optional

from .user import User


@dataclass
class Overwrite:
    id: str
    type: int
    allow: str
    deny: str


@dataclass
class ThreadMetadata:
    archived: bool
    auto_archive_duration: int
    archive_timestamp: str
    locked: bool
    invitable: Optional[bool]


@dataclass
class ThreadMember:
    id: Optional[str]
    user_id: Optional[str]
    join_timestamp: str
    flags: int


@dataclass
class Channel:
    id: str
    type: int
    guild_id: Optional[str]
    position: Optional[int]
    permission_overwrites: Optional[Overwrite]
    name: Optional[str]
    topic: Optional[str]
    nsfw: Optional[bool]
    last_message_id: Optional[str]
    bitrate: Optional[int]
    user_limit: Optional[int]
    rate_limit_per_user: Optional[int]
    recipients: Optional[list[User]]
    icon: Optional[str]
    owner_id: Optional[str]
    application_id: Optional[str]
    parent_id: Optional[str]
    last_pin_timestamp: Optional[str]
    rtc_region: Optional[str]
    video_quality_mode: Optional[int]
    message_count: Optional[int]
    member_count: Optional[int]
    thread_metadata: Optional[ThreadMetadata]
    member: Optional[ThreadMember]
    default_auto_archive_duration: Optional[int]
    permissions: Optional[str]
