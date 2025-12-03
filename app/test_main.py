from unittest import mock
from unittest.mock import Mock

from app.main import can_access_google_page

URL = "https://www.google.com"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True

    assert can_access_google_page(URL) == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_but_no_internet(
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock

) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True

    assert can_access_google_page(URL) == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_invalid_url_but_internet_exists(
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock

) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False

    assert can_access_google_page(URL) == "Not accessible"
