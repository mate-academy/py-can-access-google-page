from app.main import can_access_google_page
from unittest import mock
import pytest


@pytest.fixture(scope="function")
def mocked_get_url() -> mock:
    with mock.patch("app.main.valid_google_url") as valid_google_url:
        yield valid_google_url


@pytest.fixture(scope="function")
def mocked_get_connection() -> mock:
    with (mock.patch("app.main.has_internet_connection")
          as mocked_connection_check):
        yield mocked_connection_check


@pytest.mark.parametrize(
    "mocked_url, mocked_connection, result",
    [
        pytest.param(True, True, "Accessible",
                     id="test valid url and connection exists"),
        pytest.param(True, False, "Not accessible",
                     id="url valid but connection does not exists"),
        pytest.param(False, True, "Not accessible",
                     id="url not valid but connection exists"),
        pytest.param(False, False, "Not accessible",
                     id="both url and connection return false"),
    ]
)
def test_can_access_google_page(mocked_get_url: mock,
                                mocked_get_connection: mock,
                                mocked_url: bool,
                                mocked_connection: bool,
                                result: str) -> None:
    mocked_get_url.return_value = mocked_url
    mocked_get_connection.return_value = mocked_connection
    assert can_access_google_page("google.com") == result
