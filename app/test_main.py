from unittest import mock

from app.main import can_access_google_page


def test_have_internet_and_correct_url() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as valid_url_mock,
        mock.patch("app.main.valid_google_url") as has_internet_mock,
    ):
        has_internet_mock.return_value = True
        valid_url_mock.return_value = True
        assert can_access_google_page("https://www.google.com") == "Accessible"


def test_dont_have_internet_and_correct_url() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as valid_url_mock,
        mock.patch("app.main.valid_google_url") as has_internet_mock,
    ):
        has_internet_mock.return_value = False
        valid_url_mock.return_value = True
        assert (
            can_access_google_page("https://www.google.com")
            == "Not accessible"
        )


def test_have_internet_and_incorrect_url() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as valid_url_mock,
        mock.patch("app.main.valid_google_url") as has_internet_mock,
    ):
        has_internet_mock.return_value = True
        valid_url_mock.return_value = False
        assert (
            can_access_google_page("https://www.google.com")
            == "Not accessible"
        )


def test_dont_have_internet_and_incorrect_url() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as valid_url_mock,
        mock.patch("app.main.valid_google_url") as has_internet_mock,
    ):
        has_internet_mock.return_value = False
        valid_url_mock.return_value = False
        assert (
            can_access_google_page("https://www.google.com")
            == "Not accessible"
        )
