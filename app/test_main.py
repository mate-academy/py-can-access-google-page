from unittest.mock import patch, Mock
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_when_url_is_valid_and_connection_exist(
        mock_url: Mock,
        mock_connection: Mock) -> None:
    mock_url.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page("url") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_valid_url_and_no_internet_connection(
        mock_url: Mock,
        mock_connection: Mock) -> None:
    mock_url.return_value = True
    mock_connection.return_value = False
    assert can_access_google_page("url") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_connection_exist_and_url_is_not_valid(
        mock_url: Mock,
        mock_connection: Mock) -> None:
    mock_url.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page("url") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_url_is_not_valid_and_no_internet_connection(
        mock_url: Mock,
        mock_connection: Mock) -> None:
    mock_url.return_value = False
    mock_connection.return_value = False
    assert can_access_google_page("url") == "Not accessible"
