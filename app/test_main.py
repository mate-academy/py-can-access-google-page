from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_both_valid(mock_internet: MagicMock, mock_url: MagicMock) -> None:
    mock_url.return_value = True
    mock_internet.return_value = True
    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_url_not_valid_but_internet_exists(
        mock_internet: MagicMock,
        mock_url: MagicMock
) -> None:
    mock_url.return_value = False
    mock_internet.return_value = True
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_url_valid_but_no_internet(
        mock_internet: MagicMock,
        mock_url: MagicMock
) -> None:
    mock_url.return_value = True
    mock_internet.return_value = False
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_both_invalid(mock_internet: MagicMock, mock_url: MagicMock) -> None:
    mock_url.return_value = False
    mock_internet.return_value = False
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"
