from unittest import mock

from app.main import can_access_google_page


def test_valid_google_url_exists() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        can_access_google_page("https://mate.academy")
        mocked_url.assert_called_once()


def test_has_internet_connection_exists() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        can_access_google_page("https://mate.academy")
        mocked_connection.assert_called_once()
