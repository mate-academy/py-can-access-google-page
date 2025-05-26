from .main import can_access_google_page
from unittest import mock


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_url: bool,
        mock_internet: bool) -> None:
    mock_internet.return_value = True
    mock_valid_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_with_invalid_url(
        mock_valid_url: bool,
        mock_internet: bool) -> None:
    mock_internet.return_value = True
    mock_valid_url.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_has_no_internet(
        mock_valid_url: bool,
        mock_internet: bool) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
