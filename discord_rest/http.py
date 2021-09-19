from dataclasses import dataclass, field
from typing import Literal, Union

import requests

from . import __version__


@dataclass
class HTTPRqeuest:
    method: Literal["GET", "POST", "PATCH", "PUT", "DELETE"]
    endpoint: str
    query: dict[str, Union[str, int, bool]] = field(default_factory=dict)

    def __post_init__(self):
        for key, value in self.query.copy().items():

            if not isinstance(value, bool):
                continue

            self.query[key] = int(value)


API_VERSION = 9
BASE_ENDPOINT = f"https://discord.com/api/v{API_VERSION}"


class HTTPClient:
    def __init__(self, token: str) -> None:
        self.headers = {
            "User-Agent": f"DiscordBot (https://github.com/chun37/discord-rest.py, {__version__})",
            "Authorization": f"Bot {token}",
        }

    def send(self, req: HTTPRqeuest):
        res = requests.request(
            req.method,
            BASE_ENDPOINT + req.endpoint,
            headers=self.headers,
            params=req.query,
        )
        res.raise_for_status()
        return res
