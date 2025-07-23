from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_accessible_when_valid_url_and_internet(
        mock_internet: bool, mock_valid_url: bool) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True

    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_invalid_url(
        mock_internet: bool, mock_valid_url: bool) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = True

    result = can_access_google_page("https://invalid-url.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_no_internet(
        mock_internet: bool, mock_valid_url: bool) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = False

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_invalid_url_and_no_internet(
        mock_internet: bool, mock_valid_url: bool) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = False

    result = can_access_google_page("https://invalid-url.com")
    assert result == "Not accessible"
