import pytest
import requests

from discord_rest.models.guild import Guild
from discord_rest.client import Client
from discord_rest.request import GetGuildRequest


with open("../.env") as f:
    token = f.read().strip()

client = Client(token)


@pytest.mark.parametrize(
    "guild_id", ["772714095035154434", "605651676572942336", "414625643045584906"]
)
def test_decode_guild(
    guild_id,
):

    result = client.get_guild(GetGuildRequest(guild_id))

    assert isinstance(result, Guild)


def test_not_found_guild():
    with pytest.raises(requests.exceptions.HTTPError):
        client.get_guild(GetGuildRequest("0"))
