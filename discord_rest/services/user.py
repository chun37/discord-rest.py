import typedjson

from ..http import HTTPClient, HTTPRqeuest
from ..models import User
from ..request import GetUserRequest


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

    def get_user(self, data: GetUserRequest) -> User:
        req = HTTPRqeuest("GET", f"/users/{data.id}")
        res = self._http.send(req)

        result = typedjson.decode(User, res.json())
        if isinstance(result, typedjson.DecodingError):
            raise result

        return result
