from .http import HTTPClient
from .models import Guild, User
from .request import GetGuildRequest, GetUserRequest
from .services import GuildService, UserService


class Client:
    def __init__(self, token: str) -> None:
        self._http = HTTPClient(token)
        self._guild = GuildService(self._http)
        self._user = UserService(self._http)

    def get_guild(self, data: GetGuildRequest) -> Guild:
        return self._guild.get_guild(data)

    def get_current_user(self) -> User:
        return self._user.get_current_user()

    def get_user(self, data: GetUserRequest) -> User:
        return self._user.get_user(data)
