from unittest import mock
from unittest.mock import Mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
def test_valid_google_url_has_called(mocked_valid_url: Mock) -> None:
    url = "http://google.com"
    can_access_google_page(url)
    mocked_valid_url.assert_called_once_with(url)


@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection_has_called(
        mocked_has_connection: Mock
) -> None:
    url = "http://google.com"
    can_access_google_page(url)
    mocked_has_connection.assert_called_once()
