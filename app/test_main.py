from unittest import mock

from app.main import can_access_google_page


def test_function_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        can_access_google_page("https://google.com")
        mocked_connection.assert_called_once()


def test_function_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        can_access_google_page("https://google.com")
        mocked_valid_url.assert_called_once_with("https://google.com")
