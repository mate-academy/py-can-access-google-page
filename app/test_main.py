from unittest.mock import MagicMock, patch
from app.main import can_access_google_page

@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_accessible(
    mock_internet: MagicMock,
    mock_valid: MagicMock
) -> None:
    mock_valid.return_value = True
    mock_internet.return_value = True
    result = can_access_google_page("https://google.com")
    assert result == "Accessible"

@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_invalid_url(
    mock_internet: MagicMock,
    mock_url: MagicMock
) -> None:
    mock_url.return_value = False
    mock_internet.return_value = True
    result = can_access_google_page("https://bad-site.com")
    assert result == "Not accessible"

@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_no_internet_connection(
    mock_internet: MagicMock,
    mock_url: MagicMock
) -> None:
    mock_url.return_value = True
    mock_internet.return_value = False
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"

@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_invalid_url_and_no_internet(
    mock_internet: MagicMock,
    mock_url: MagicMock
) -> None:
    mock_url.return_value = False
    mock_internet.return_value = False
    result = can_access_google_page("https://bad-site.com")
    assert result == "Not accessible"
