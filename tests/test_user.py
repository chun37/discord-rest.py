import pytest
import requests

from discord_rest.models import User
from discord_rest import Client, GetUserRequest


with open("../.env") as f:
    token = f.read().strip()

client = Client(token)


def test_get_current_user():
    assert isinstance(client.get_current_user(), User)


@pytest.mark.parametrize("user_id", ["311536274462867476", "514397938999492609"])
def test_get_user(user_id):
    result = client.get_user(GetUserRequest(user_id))
    assert isinstance(result, User)


def test_get_not_found_user():
    with pytest.raises(requests.exceptions.HTTPError):
        client.get_user(GetUserRequest("0"))
