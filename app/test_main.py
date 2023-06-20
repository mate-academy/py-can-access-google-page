from typing import Callable
from unittest.mock import patch

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, connection, result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        ("`can_access_google_page` should return "
         "`Accessible` when has connection & url is valid"),
        ("`can_access_google_page` should return "
         "`Not accessible` when has connection but url is not valid"),
        ("`can_access_google_page` should return "
         "`Not accessible` when has no connection but url is valid"),
        ("`can_access_google_page` should return "
         "`Not accessible` when no connection & url is not valid")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_url: Callable,
        mocked_connection: Callable,
        url: bool,
        connection: bool,
        result: str
) -> None:
    mocked_url.return_value = url
    mocked_connection.return_value = connection
    action = can_access_google_page("https://www.google.com/")
    assert action == result
