from dataclasses import dataclass


@dataclass
class StageInstance:
    id: str
    guild_id: str
    channel_id: str
    topic: str
    privacy_level: int
    discoverable_disabled: bool
