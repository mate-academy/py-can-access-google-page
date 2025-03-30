from unittest import mock
import app.main
from app.main import (
    can_access_google_page,
)


def test_return_function_value() -> None:
    assert can_access_google_page("http://google.com") == "Accessible"


def test_has_internet_connection_was_called() -> None:
    app.main.has_internet_connection = mock.MagicMock()
    can_access_google_page("http://google.com")
    app.main.has_internet_connection.assert_called_once()


def test_valid_google_url_was_called() -> None:
    app.main.valid_google_url = mock.MagicMock()
    can_access_google_page("http://google.com")
    app.main.valid_google_url.assert_called_once_with("http://google.com")


def test_cannot_access_if_connection_or_valid_url_is_true() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        with mock.patch("app.main.valid_google_url") as mocked_valid_url:
            mocked_connection.return_value = False
            mocked_valid_url.return_value = False
            assert (can_access_google_page("http://google.com")
                    == "Not accessible")


def test_cannot_access_if_only_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        with mock.patch("app.main.valid_google_url") as mocked_valid_url:
            mocked_connection.return_value = True
            mocked_valid_url.return_value = False
            result = can_access_google_page("http://google.com")
    assert result == "Not accessible"


def test_cannot_access_if_only_valid_url() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        with mock.patch("app.main.valid_google_url") as mocked_valid_url:
            mocked_connection.return_value = False
            mocked_valid_url.return_value = True
            result = can_access_google_page("http://google.com")
    assert result == "Not accessible"
