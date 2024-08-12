import pytest
from unittest.mock import patch, MagicMock
import datetime
import requests
from app.main import can_access_google_page


@pytest.fixture
def mock_valid_google_url():
    with patch("app.main.valid_google_url") as mock:
        yield mock


@pytest.fixture
def mock_has_internet_connection():
    with patch("app.main.has_internet_connection") as mock:
        yield mock


@pytest.mark.parametrize(
    "valid_url_return, internet_connection_return, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
    valid_url_return: bool,
    internet_connection_return: bool,
    expected_result: str,
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
) -> None:
    mock_valid_google_url.return_value = valid_url_return
    mock_has_internet_connection.return_value = internet_connection_return

    url = "https://www.google.com"
    result = can_access_google_page(url)

    assert result == expected_result
