from unittest import mock

from app.main import can_access_google_page


def test_of_calling_has_internet_connection() -> None:
    with (
        mock.patch("app.main.has_internet_connection")
        as mocked_has_internet_connection
    ):

        can_access_google_page("https://www.google.com/")
        mocked_has_internet_connection.assert_called_once()


def test_of_calling_valid_google_url() -> None:
    with (
        mock.patch("app.main.valid_google_url")
        as mocked_has_internet_connection
    ):

        can_access_google_page("https://www.google.com/")
        mocked_has_internet_connection.assert_called_once()
