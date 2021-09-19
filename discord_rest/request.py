from dataclasses import dataclass


@dataclass
class GetGuildRequest:
    id: str
    with_counts: bool = False


@dataclass
class GetUserRequest:
    id: str
