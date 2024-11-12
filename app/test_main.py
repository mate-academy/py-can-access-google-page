import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


@pytest.fixture()
def mocked_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


@pytest.mark.parametrize(
    "valid_url, internet_connection, expected", [
        pytest.param(
            True, True, "Accessible",
            id="Accessible"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="Should return 'not accessible' while no internet"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="Should return 'not accessible' with invalid url"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="Should return 'not accessible' with invalid url "
               "and no internet"
        )
    ]
)
def test_can_access_google_page(mocked_valid_url: callable,
                                mocked_internet_connection: callable,
                                valid_url: bool,
                                internet_connection: bool,
                                expected: str) -> None:
    mocked_valid_url.return_value = valid_url
    mocked_internet_connection.return_value = internet_connection
    assert can_access_google_page("http://google.com") == expected
