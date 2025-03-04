from pytest import fixture, mark
from unittest.mock import patch

from app.main import can_access_google_page


@fixture
def mocked_dependencies():
    with (patch("app.main.valid_google_url") as valid_google_url,
          patch("app.main.has_internet_connection") as has_internet_connection):
        yield valid_google_url, has_internet_connection


@mark.parametrize(
    "has_connection, valid_url, result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
    ],
    ids=[
        "test should access if both arguments are true",
        "test should not access if both arguments are false",
        "test should not access if no connection",
        "test should not access if url is invalid"
    ]

)
def test_can_access_google_page(mocked_dependencies, has_connection, valid_url, result):
    valid_google_url, has_internet_connection = mocked_dependencies

    valid_google_url.return_value = valid_url
    has_internet_connection.return_value = has_connection

    assert can_access_google_page("https://google.com") == result
