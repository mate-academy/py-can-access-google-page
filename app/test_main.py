from typing import Callable
from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection_return,valid_url_return,expected_result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ],
    ids=[
        "can't access only with connection",
        "can't access only with valid url",
        "can't access with no connection and valid url",
        "can access with connection and valid url"
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_access_google_page(
        mock_internet_connection: Callable,
        mock_valid_google_url: Callable,
        connection_return: bool,
        valid_url_return: bool,
        expected_result: str
) -> None:
    mock_internet_connection.return_value = connection_return
    mock_valid_google_url.return_value = valid_url_return
    assert can_access_google_page("https://google.com") == expected_result
