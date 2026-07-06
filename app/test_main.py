from typing import Any
from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_when_both_true(
        mock_valid_google_url: Any,
        mock_has_internet_connection: Any
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_when_both_false(
        mock_valid_google_url: Any,
        mock_has_internet_connection: Any
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    result = can_access_google_page("https")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_when_internet_false(
        mock_valid_google_url: Any,
        mock_has_internet_connection: Any
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_when_url_false(
        mock_valid_google_url: Any,
        mock_has_internet_connection: Any
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    result = can_access_google_page("https")
    assert result == "Not accessible"
