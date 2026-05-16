from unittest import mock
import pytest


@pytest.fixture()
def google_page_url() -> str:
    url = "https://www.google.com/"
    return url


def test_valid_google_url(google_page_url: str) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_google_url:
        mocked_valid_google_url.return_value = "Accessible"
        assert mocked_valid_google_url(google_page_url) == "Accessible"


def test_has_internet_connection(google_page_url: str) -> None:
    with mock.patch(
        "app.main.has_internet_connection"
    ) as mocked_has_internet_connection:
        mocked_has_internet_connection.return_value = True
        assert mocked_has_internet_connection() is True
