# write your code here
from unittest import mock

from app.main import can_access_google_page

url = "https://google.com"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_no_internet_connection_valid_url(
        mock_valid_google_url: object,
        mock_has_internet_connection: object
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page(url) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_internet_connection_available_valid_url(
        mock_valid_google_url: object,
        mock_has_internet_connection: object
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page(url) == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_no_internet_connection_invalid_url(
        mock_valid_google_url: object,
        mock_has_internet_connection: object
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    assert can_access_google_page(url) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_internet_connection_available_invalid_url(
        mock_valid_google_url: object,
        mock_has_internet_connection: object
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page(url) == "Not accessible"
