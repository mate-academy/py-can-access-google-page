from unittest import mock
from typing import Any

from app.main import can_access_google_page


def test_can_access_google_page_accessible() -> None:
    assert can_access_google_page(
        "https://www.google.com.ua/?hl=ukar"
    ) == "Accessible"


@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_not_accessible(
        mocked_valid_google_url: Any
) -> None:
    mocked_valid_google_url.return_value = False
    assert can_access_google_page(
        "https://www.goosdofighoidjfggle.com.ua/?hl=uk"
    ) == "Not accessible"


@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection_not_accessible(
        mocked_has_internet_connection: Any
) -> None:
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page(
        "https://www.goosdofighoidkjhihjfggle.com.ua/?hl=uk"
    ) == "Not accessible"
