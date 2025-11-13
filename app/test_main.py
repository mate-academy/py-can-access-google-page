from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_accessible_when_url_valid_and_internet(
    mock_valid_url: MagicMock, mock_internet: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_not_accessible_when_url_invalid(
    mock_valid_url: MagicMock, mock_internet: MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_not_accessible_when_no_internet(
    mock_valid_url: MagicMock, mock_internet: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_not_accessible_when_no_internet_and_url_invalid(
    mock_valid_url: MagicMock, mock_internet: MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
