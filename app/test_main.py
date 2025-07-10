from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> any:
    with mock.patch("app.main.valid_google_url") as mock_test_valid_google_url:
        yield mock_test_valid_google_url


@pytest.fixture()
def mocked_has_internet_connection() -> any:
    with mock.patch(
        "app.main.has_internet_connection"
    ) as mock_test_has_internet_connection:
        yield mock_test_has_internet_connection


@pytest.mark.parametrize(
    "valid_url, internet_connection, result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="if url is valid and has internet connection"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="if url is not valid and has internet connection",
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="if url is valid and has no internet connection",
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="if url is not valid and has no internet connection",
        ),
    ],
)
def test_can_access_google_url(
    mocked_valid_google_url: any,
    mocked_has_internet_connection: any,
    valid_url: bool,
    internet_connection: bool,
    result: str,
) -> None:
    mocked_valid_google_url.return_value = valid_url
    mocked_has_internet_connection.return_value = internet_connection
    assert can_access_google_page("https://www.google.com/") == result
