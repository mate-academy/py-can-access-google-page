from app.main import can_access_google_page
import pytest
from unittest import mock


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("valid_google_url()") as google_url:
        yield google_url


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch("has_internet_connection()") as internet_connection:
        yield internet_connection


def test_can_access_google_page(
    mocked_valid_google_url: None,
    mocked_has_internet_connection: None
) -> None:
    mocked_valid_google_url.assert_called_once()
    mocked_has_internet_connection.assert_called_once()
    assert can_access_google_page("https://www.google.com") == "Accessible"
