from unittest.mock import patch, Mock
from app import main


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_valid_url_internet_connection_is_ok(
        mock_has_internet_connection: Mock,
        mock_valid_google_url: Mock
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True
    result = main.can_access_google_page("https://google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_valid_url_no_internet_connection(
        mock_has_internet_connection: Mock,
        mock_valid_google_url: Mock
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True
    result = main.can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_valid_url_internet_connection_is_ok(
        mock_has_internet_connection: Mock,
        mock_valid_google_url: Mock
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False
    result = main.can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_valid_url_no_internet_connection(
        mock_has_internet_connection: Mock,
        mock_valid_google_url: Mock
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = False
    result = main.can_access_google_page("https://google.com")
    assert result == "Not accessible"
