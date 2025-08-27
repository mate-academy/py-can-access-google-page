from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_returns_accessible_when_valid_url_and_internet(
        mock_valid_google: MagicMock,
        mock_has_internet: MagicMock) -> None:
    mock_valid_google.return_value = True
    mock_has_internet.return_value = True
    result = can_access_google_page("https://example.com")
    assert result == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_returns_not_accessible_when_invalid_url(
        mock_valid_google: MagicMock,
        mock_has_internet: MagicMock) -> None:
    mock_valid_google.return_value = False
    mock_has_internet.return_value = True
    result = can_access_google_page("https://example.com")
    assert result == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_returns_not_accessible_when_no_internet(
        mock_valid_google: MagicMock,
        mock_has_internet: MagicMock) -> None:
    mock_valid_google.return_value = True
    mock_has_internet.return_value = False
    result = can_access_google_page("https://example.com")
    assert result == "Not accessible"
