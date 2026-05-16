from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def google_page_url() -> str:
    url = "https://www.google.com/"
    return url


def test_accessible_google_page(google_page_url: str) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid:
        with mock.patch(
            "app.main.has_internet_connection"
        ) as mocked_internet:
            mocked_valid.return_value = True
            mocked_internet.return_value = True

            result = can_access_google_page(google_page_url)

            assert result == "Accessible"


def test_invalid_google_url(google_page_url: str) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid:
        with mock.patch(
            "app.main.has_internet_connection"
        ) as mocked_internet:
            mocked_valid.return_value = False
            mocked_internet.return_value = True

            result = can_access_google_page(google_page_url)

            assert result == "Not accessible"


def test_no_internet_connection(google_page_url: str) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid:
        with mock.patch(
            "app.main.has_internet_connection"
        ) as mocked_internet:
            mocked_valid.return_value = True
            mocked_internet.return_value = False

            result = can_access_google_page(google_page_url)

            assert result == "Not accessible"


def test_invalid_url_and_no_internet(
    google_page_url: str,
) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid:
        with mock.patch(
            "app.main.has_internet_connection"
        ) as mocked_internet:
            mocked_valid.return_value = False
            mocked_internet.return_value = False

            result = can_access_google_page(google_page_url)

            assert result == "Not accessible"
