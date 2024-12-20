from unittest import mock
from unittest.mock import MagicMock

from app.main import (can_access_google_page,
                      has_internet_connection,
                      valid_google_url)


@mock.patch("requests.get")
def test_valid_google_url(mocked_get: MagicMock) -> None:
    mocked_get.return_value.status_code = 200
    assert valid_google_url("http://google.com") is True
    mocked_get.assert_called_once_with("http://google.com")


@mock.patch("datetime.datetime")
def test_has_internet_connection(mocked_datetime: MagicMock) -> None:
    mocked_datetime.now.return_value.hour = 10
    assert has_internet_connection() is True

    mocked_datetime.now.return_value.hour = 5
    assert has_internet_connection() is False
    mocked_datetime.now.assert_called()


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_internet: MagicMock,
                                mocked_google: MagicMock) -> None:
    mocked_internet.return_value = True
    mocked_google.return_value = True
    assert can_access_google_page("https:/google.com") == "Accessible"

    mocked_google.return_value = False
    mocked_internet.return_value = True
    assert can_access_google_page("http://google.com") == "Not accessible"

    mocked_internet.return_value = True
    mocked_google.return_value = False
    assert can_access_google_page("http://google.com") == "Not accessible"
