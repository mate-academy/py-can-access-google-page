from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mock_has_internet_connection: mock,
        mock_valid_google_url: mock) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_url_with_connection(
        mock_has_internet_connection: mock,
        mock_valid_google_url: mock) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    result = can_access_google_page("https://invalid-url.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_no_connection(
        mock_has_internet_connection: mock,
        mock_valid_google_url: mock) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
