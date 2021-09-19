from dataclasses import dataclass
from typing import Optional

from .member import Member


@dataclass
class VoiceState:
    guild_id: Optional[str]
    channel_id: Optional[str]
    user_id: str
    member: Optional[Member]
    session_id: str
    deaf: bool
    mute: bool
    self_deaf: bool
    self_mute: bool
    self_stream: Optional[bool]
    self_video: bool
    suppress: bool
    request_to_speak_timestamp: Optional[str]
