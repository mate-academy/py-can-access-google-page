from app.main import can_access_google_page, \
    valid_google_url, has_internet_connection
from unittest import mock
import datetime


def test_correct_google_url() -> None:
    assert valid_google_url("http://google.com") is True


def test_internet_connection() -> None:
    current_time = datetime.datetime.now()
    if current_time.hour in range(6, 23):
        assert has_internet_connection() is True
    else:
        assert has_internet_connection() is False


def test_can_access_google_page() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        with mock.patch("app.main.has_internet_connection") \
                as mocked_internet_connection:
            can_access_google_page("http://google.com")
            mocked_internet_connection.assert_called_once()
        mocked_url.assert_called_once()
