from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_internet_connection() -> mock.MagicMock:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


@pytest.fixture()
def mocked_valid_google_url() -> mock.MagicMock:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        yield mocked_valid_url


@pytest.mark.parametrize(
    "internet_status,valid_url,expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "Valid URL with internet connection - should be accessible",
        "Invalid URL with internet connection - should not be accessible",
        "Valid URL without internet connection - should not be accessible",
        "Invalid URL and no internet connection - should not be accessible",
    ]
)
def test_can_access_google_page(
        mocked_internet_connection: object,
        mocked_valid_google_url: object,
        internet_status: bool,
        valid_url: bool,
        expected_result: str
) -> None:
    mocked_valid_google_url.return_value = valid_url
    mocked_internet_connection.return_value = internet_status
    assert can_access_google_page("https://www.google.com") == expected_result
