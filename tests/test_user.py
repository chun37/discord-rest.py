from discord_rest.models import User
from discord_rest.client import Client


with open("../.env") as f:
    token = f.read().strip()

client = Client(token)


def test_get_current_user():
    assert isinstance(client.get_current_user(), User)
