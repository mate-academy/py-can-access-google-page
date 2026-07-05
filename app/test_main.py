from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_accessible(mock_internet: MagicMock, mock_url: MagicMock) -> None:
    mock_url.return_value = True
    mock_internet.return_value = True
    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_url(mock_internet: MagicMock, mock_url: MagicMock) -> None:
    mock_url.return_value = False
    mock_internet.return_value = True
    result = can_access_google_page("https://gooogle_.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_internet_connectivity(
        mock_internet: MagicMock,
        mock_url: MagicMock) -> None:
    mock_url.return_value = True
    mock_internet.return_value = False
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"
