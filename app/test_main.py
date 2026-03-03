from app.main import can_access_google_page
from unittest import mock


def test_valid_url_and_has_internet_connection() -> None:
    with mock.patch(
            "app.main.has_internet_connection",
            return_value=True
    ):
        with mock.patch(
                "app.main.valid_google_url",
                return_value=True
        ):
            assert can_access_google_page(
                "https://www.google.com"
            ) == "Accessible"


def test_valid_url_and_no_internet_connection() -> None:
    with mock.patch(
            "app.main.valid_google_url",
            return_value=True
    ):
        with mock.patch(
                "app.main.has_internet_connection",
                return_value=False
        ):
            assert can_access_google_page(
                "https://www.google.com"
            ) == "Not accessible"


def test_invalid_url_and_has_internet_connection() -> None:
    with mock.patch(
            "app.main.valid_google_url",
            return_value=False
    ):
        with mock.patch(
                "app.main.has_internet_connection",
                return_value=True
        ):
            assert can_access_google_page(
                "https://www.google.com"
            ) == "Not accessible"


def test_invalid_url_and_no_internet_connection() -> None:
    with mock.patch(
            "app.main.valid_google_url",
            return_value=False
    ):
        with mock.patch(
                "app.main.has_internet_connection",
                return_value=False
        ):
            assert can_access_google_page(
                "https://www.google.com"
            ) == "Not accessible"
