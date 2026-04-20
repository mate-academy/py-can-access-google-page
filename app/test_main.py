from unittest import mock

from app.main import can_access_google_page


def test_can_access_google_page_accessible() -> None:
    with (
        mock.patch("app.main.valid_google_url") as mocked_valid,
        mock.patch("app.main.has_internet_connection") as mocked_connection
    ):
        mocked_valid.return_value = True
        mocked_connection.return_value = True
        result = can_access_google_page("https://google.com")
        assert result == "Accessible"


def test_can_access_google_page_not_accessible_first_case() -> None:
    with (
        mock.patch("app.main.valid_google_url") as mocked_valid,
        mock.patch("app.main.has_internet_connection") as mocked_connection
    ):
        mocked_valid.return_value = False
        mocked_connection.return_value = True
        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"


def test_can_access_google_page_not_accessible_second_case() -> None:
    with (
        mock.patch("app.main.valid_google_url") as mocked_valid,
        mock.patch("app.main.has_internet_connection") as mocked_connection
    ):
        mocked_valid.return_value = True
        mocked_connection.return_value = False
        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"
