import pytest
from typing import Callable
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "can access when valid url and has internet",
        "can't access when valid url, but no internet",
        "can't access with internet, but invalid url",
        "can't access with invalid url and no internet",
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: Callable,
        mock_valid_google_url: Callable,
        valid_url: bool,
        internet_connection: bool,
        expected_result: str
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = internet_connection

    result = can_access_google_page("www.google.com")

    assert result == expected_result
