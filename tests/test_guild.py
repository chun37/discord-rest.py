import pytest
import requests

from discord_rest import Client
from discord_rest.models import Guild, PartialGuild
from discord_rest.request import GetGuildRequest

with open("../.env") as f:
    token = f.read().strip()

client = Client(token)


@pytest.mark.parametrize(
    "guild_id", ["772714095035154434", "605651676572942336", "414625643045584906"]
)
def test_get_guild(
    guild_id,
):

    result = client.get_guild(GetGuildRequest(guild_id))

    assert isinstance(result, Guild)


def test_get_not_found_guild():
    with pytest.raises(requests.exceptions.HTTPError):
        client.get_guild(GetGuildRequest("0"))


def test_get_current_user_guilds():
    result = client.get_current_user_guilds()

    assert isinstance(result, list)
    if len(result) > 0:
        assert isinstance(result[0], PartialGuild)
