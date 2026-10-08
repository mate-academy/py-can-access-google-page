from unittest import mock
from unittest.mock import Mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: Mock,
        mock_valid_google_url: Mock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_google_url_fails(
        mock_has_internet_connection: Mock,
        mock_valid_google_url: Mock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection_fails(
        mock_has_internet_connection: Mock,
        mock_valid_google_url: Mock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_fails(
        mock_has_internet_connection: Mock,
        mock_valid_google_url: Mock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"
