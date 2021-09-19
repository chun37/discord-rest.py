from dataclasses import dataclass


@dataclass(frozen=True)
class Emoji:
    name: str
    roles: list[str]
    id: str
    require_colons: bool
    managed: bool
    animated: bool
    available: bool
