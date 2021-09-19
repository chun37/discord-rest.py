import typedjson

from ..http import HTTPClient, HTTPRqeuest
from ..models import User


class UserService:
    def __init__(self, http: HTTPClient):
        self._http = http

    def get_current_user(self) -> User:
        req = HTTPRqeuest("GET", "/users/@me")
        res = self._http.send(req)

        result = typedjson.decode(User, res.json())
        if isinstance(result, typedjson.DecodingError):
            raise result

        return result
