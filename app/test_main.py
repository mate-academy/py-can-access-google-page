from pytest import fixture, mark
from unittest import mock

from app.main import (
    can_access_google_page
)

some_url = "https://www.google.com"


@fixture()
def mocked_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_test_url:
        yield mocked_test_url


@fixture()
def mocked_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_test_connect:
        yield mocked_test_connect


@mark.parametrize(
    "google_response,connection_response,expected_result",
    [
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (True, True, "Accessible")
    ],
    ids=[
        "Not accessible when has no internet connection and valid google url",
        "Not accessible when has no valid google url",
        "Not accassible when has no internet connection",
        "Accessible when has both internet connection and valid google url"
    ]
)
def test_check_if_can_access_google_page(
        google_response: str,
        connection_response: str,
        expected_result: str,
        mocked_connection: mock,
        mocked_url: mock
) -> None:
    mocked_url.return_value = google_response
    mocked_connection.return_value = connection_response
    result = can_access_google_page(some_url)
    assert result == expected_result


def test_check_if_url_fuctions_is_called(mocked_url: mock) -> None:
    can_access_google_page(some_url)
    mocked_url.assert_called_once()


def test_check_if_connection_fuctions_is_called(
        mocked_connection: mock
) -> None:

    can_access_google_page(some_url)
    mocked_connection.assert_called_once()
