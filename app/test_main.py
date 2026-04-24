from app.main import can_access_google_page
from unittest.mock import patch


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_should_return_accessible_when_url_valid_and_has_internet(
        mock_valid_google_url: bool,
        mock_has_internet_connection: bool
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_should_return_not_accessible_when_url_not_valid_and_has_internet(
        mock_valid_google_url: bool,
        mock_has_internet_connection: bool) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    result = can_access_google_page("https://www.non.valid.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_should_return_not_accessible_when_url_valid_and_no_internet(
        mock_valid_google_url: bool,
        mock_has_internet_connection: bool) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_should_return_not_accessible_when_url_not_valid_and_no_internet(
        mock_valid_google_url: bool,
        mock_has_internet_connection: bool) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    result = can_access_google_page("https://www.non.valid.com")
    assert result == "Not accessible"
