import pytest

from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_connection() -> mock:
    with (mock.patch("app.main.has_internet_connection")
          as mock_connection):
        yield mock_connection


@pytest.fixture()
def mocked_url() -> mock:
    with mock.patch("app.main.valid_google_url") as mock_test_url:
        yield mock_test_url


def test_valid_url_and_connection_exists(
        mocked_url: mock,
        mocked_connection: mock
) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = True

    result = can_access_google_page("https://www.python.org")

    mocked_url.assert_called_once_with("https://www.python.org")
    mocked_connection.assert_called_once()

    assert result == "Accessible"
