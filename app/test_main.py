from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_has_valid_url() -> mock:
    with mock.patch(
            "app.main.valid_google_url"
    ) as mock_test_valid_url:
        yield mock_test_valid_url


@pytest.fixture()
def mocked_has_ethernet() -> mock:
    with mock.patch(
            "app.main.has_internet_connection"
    ) as has_internet_connection:
        yield has_internet_connection


@pytest.mark.parametrize(
    "url, connection, result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible"),
        (False, False, "Not accessible")
    ], ids=[
        "In case of no connection is expected 'Not accessible'",
        "If the URL is incorrect and"
        "the connection already exists is expected 'Not accessible'",
        "In case of valid URL and"
        "connection already exists is expected 'Accessible'",
        "In case of no connection and invalid URL is expected 'Not accessible'"
    ]
)
def test_valid_url_and_connection_not_exists(
        url: bool,
        connection: bool,
        result: str,
        mocked_has_valid_url: mock,
        mocked_has_ethernet: mock
) -> None:
    mocked_has_valid_url.return_value = url
    mocked_has_ethernet.return_value = connection
    assert can_access_google_page("some.url") == result
