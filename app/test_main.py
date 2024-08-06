from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_connect() -> mock.Mock:
    with mock.patch("app.main.has_internet_connection") as mock_test_connect:
        yield mock_test_connect


@pytest.fixture()
def mocked_url() -> mock.Mock:
    with mock.patch("app.main.valid_google_url") as mock_test_url:
        yield mock_test_url


@pytest.mark.parametrize(
    "has_connection, valid_url, value",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        has_connection: bool,
        valid_url: bool,
        value: str,
        mocked_connect: mock.Mock,
        mocked_url: mock.Mock
) -> None:
    mocked_connect.return_value = has_connection
    mocked_url.return_value = valid_url

    assert can_access_google_page("url") == value
