from .models.guild import Guild
from .http import HTTPClient
from .request import GetGuildRequest
from .services.guild import GuildService
from .services.user import UserService
from .models.user import User


class Client:
    def __init__(self, token: str) -> None:
        self._http = HTTPClient(token)
        self._guild = GuildService(self._http)
        self._user = UserService(self._http)

    def get_guild(self, data: GetGuildRequest) -> Guild:
        return self._guild.get_guild(data)

    def get_current_user(self) -> User:
        return self._user.get_current_user()
