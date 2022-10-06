import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_google_url() -> mock.Mock:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mocked_internet_connection() -> mock.Mock:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


@pytest.mark.parametrize(
    "valid_url,internet_connection,expected_result",
    [
        pytest.param(
            True, True, "Accessible",
            id="test should return Accessible "
               "when both checks return True"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="test should return Not accessible "
               "when both checks return False"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="test should return Not accessible "
               "when has_internet_connection() return False"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="test should return Not accessible "
               "when valid_google_url() return False"
        )
    ]
)
def test_can_access_google_page(
        mocked_google_url: mock.Mock,
        mocked_internet_connection: mock.Mock,
        valid_url: bool, internet_connection: bool,
        expected_result: str) -> None:
    mocked_google_url.return_value = valid_url
    mocked_internet_connection.return_value = internet_connection
    assert can_access_google_page("https://www.google.com/") == expected_result
