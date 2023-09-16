from unittest import mock
from app.main import can_access_google_page
import pytest


@pytest.fixture
def mocked_valid_google_url() -> mock.MagicMock:
    with mock.patch("app.main.valid_google_url") as valid_url:
        yield valid_url


@pytest.fixture
def mocked_has_internet_connection() -> mock.MagicMock:
    with mock.patch("app.main.has_internet_connection") as internet_connection:
        yield internet_connection


@pytest.mark.parametrize(
    "valid_url,has_internet_connection,result",
    [
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (True, True, "Accessible"),
        (False, False, "Not accessible")
    ]
)
def test_cannot_access_if_only_one_true(
        mocked_valid_google_url: mock.MagicMock,
        mocked_has_internet_connection: mock.MagicMock,
        valid_url: bool,
        has_internet_connection: bool,
        result: str) -> AssertionError:
    mocked_has_internet_connection.return_value = has_internet_connection
    mocked_valid_google_url.return_value = valid_url
    assert can_access_google_page("a") == result
