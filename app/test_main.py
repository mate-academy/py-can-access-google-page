from unittest.mock import patch, Mock

from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_url_valid_but_not_connection(
    mock_has_internet_connection: Mock,
    mock_valid_google_url: Mock
) -> None:
    url = "https://www.google.com"
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True
    assert can_access_google_page(url) == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_url_invalid_and_connection_exists(
    mock_has_internet_connection: Mock,
    mock_valid_google_url: Mock
) -> None:
    url = "https://www.google.com"
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False
    assert can_access_google_page(url) == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_url_invalid_and_not_connection(
    mock_has_internet_connection: Mock,
    mock_valid_google_url: Mock
) -> None:
    url = "https://www.google.com"
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = False
    assert can_access_google_page(url) == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_url_valid_and_connection_exists(
    mock_has_internet_connection: Mock,
    mock_valid_google_url: Mock
) -> None:
    url = "https://www.google.com"
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True
    assert can_access_google_page(url) == "Accessible"
