from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_when_internet_and_url_are_valid(
        mock_has_internet: MagicMock, mock_valid_url: MagicMock) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cannot_access_google_when_url_is_invalid(
        mock_has_internet: MagicMock, mock_valid_url: MagicMock) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True
    assert (can_access_google_page("https://www.fakegoogle.com")
            == "Not accessible")


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cannot_access_google_when_no_internet(
        mock_has_internet: MagicMock, mock_valid_url: MagicMock) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cannot_access_google_when_url_is_invalid_and_no_internet(
        mock_has_internet: MagicMock, mock_valid_url: MagicMock) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = False
    assert (can_access_google_page("https://www.fakegoogle.com")
            == "Not accessible")
