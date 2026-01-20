from unittest.mock import MagicMock, patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_when_url_is_valid_and_internet_is_connected(
    mock_internet: MagicMock, mock_valid_url: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cannot_access_google_page_when_only_url_is_valid(
    mock_internet: MagicMock, mock_valid_url: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cannot_access_google_page_when_only_internet_is_available(
    mock_internet: MagicMock, mock_valid_url: MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cannot_access_google_page_when_both_url_and_internet_are_invalid(
    mock_internet: MagicMock, mock_valid_url: MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
