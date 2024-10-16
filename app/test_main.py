# write your code here
from app.main import can_access_google_page
from unittest import mock


URL = "www.google.com"


def test_can_access_google_page_with_connection_and_valid_url() -> None:
    with (
        mock.patch(
            "app.main.has_internet_connection"
        ) as mocked_has_internet_connection,
        mock.patch("app.main.valid_google_url") as mocked_valid_google_url
    ):
        mocked_has_internet_connection.return_value = True
        mocked_valid_google_url.return_value = True

        assert can_access_google_page(URL) == "Accessible"


def test_can_access_google_page_without_connection() -> None:
    with (
        mock.patch(
            "app.main.has_internet_connection"
        ) as mocked_has_internet_connection,
        mock.patch("app.main.valid_google_url") as mocked_valid_google_url
    ):
        mocked_has_internet_connection.return_value = False
        mocked_valid_google_url.return_value = True

        assert can_access_google_page(URL) == "Not accessible"


def test_can_access_google_page_with_invalid_url() -> None:
    with (
        mock.patch(
            "app.main.has_internet_connection"
        ) as mocked_has_internet_connection,
        mock.patch("app.main.valid_google_url") as mocked_valid_google_url
    ):
        mocked_has_internet_connection.return_value = True
        mocked_valid_google_url.return_value = False

        assert can_access_google_page(URL) == "Not accessible"
