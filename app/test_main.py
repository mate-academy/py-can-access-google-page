from unittest import mock
from unittest.mock import MagicMock

from app.main import (can_access_google_page)

# write your code here
valid_url = "https://www.google.com/"
invalid_url = "google"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_ok(mocked_valid_google_url: MagicMock,
                                   mock_has_internet_connection: MagicMock)\
        -> None:
    assert can_access_google_page(valid_url) == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection_is_called_ok(mock_valid_google_url: MagicMock,
                                              mock_has_internet_connection:
                                              MagicMock) -> None:
    can_access_google_page(valid_url)
    mock_has_internet_connection.assert_called_once()


@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_without_internet_not_ok(
        mock_has_internet_connection: MagicMock) -> None:
    mock_has_internet_connection.return_value = False
    assert can_access_google_page(valid_url) == "Not accessible"


@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_invalid_url_not_ok(
        mock_valid_google_url: MagicMock) -> None:
    mock_valid_google_url.return_value = False
    assert can_access_google_page(invalid_url) == "Not accessible"
