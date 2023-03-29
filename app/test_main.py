from unittest import mock
from unittest.mock import MagicMock
import pytest
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> MagicMock:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        yield mocked_valid_url


@pytest.fixture()
def has_internet_connection() -> MagicMock:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


@pytest.mark.parametrize(
    "valid_url, internet_connection, expected_output",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible"),
        (False, False, "Not accessible")
    ]
)
def test_accessibility(
        mocked_valid_google_url: MagicMock,
        has_internet_connection: MagicMock,
        valid_url: bool,
        internet_connection: bool,
        expected_output: str
) -> None:
    mocked_valid_google_url.return_value = valid_url
    has_internet_connection.return_value = internet_connection
    assert can_access_google_page("test_url") == expected_output
