from typing import Callable
from unittest import mock
import pytest
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "connection, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
    mock_valid_google_url: Callable,
    mock_has_internet_connection: Callable,
    connection: bool, valid_url: bool,
    expected: str
) -> None:
    mock_has_internet_connection.return_value = connection
    mock_valid_google_url.return_value = valid_url

    result = can_access_google_page("https://example.com")
    assert result == expected
