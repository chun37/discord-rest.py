import typedjson

from ..http import HTTPClient, HTTPRqeuest
from ..request import GetGuildRequest
from ..models.guild import Guild


class GuildService:
    def __init__(self, http: HTTPClient):
        self._http = http

    def get_guild(self, data: GetGuildRequest) -> Guild:
        req = HTTPRqeuest(
            "GET", f"/guilds/{data.id}", {"with_counts": data.with_counts}
        )
        res = self._http.send(req)

        result = typedjson.decode(Guild, res.json())
        if isinstance(result, typedjson.DecodingError):
            raise result

        return result
