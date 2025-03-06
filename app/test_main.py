from pytest import fixture, mark
from unittest.mock import patch

from app.main import can_access_google_page


@fixture
def mocked_network_dependencies() -> any:
    with (patch("app.main.valid_google_url")
          as valid_google_url,
          patch("app.main.has_internet_connection")
          as has_internet_connection):
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
        "access if both arguments are true",
        "not access if both arguments are false",
        "no connection",
        "invalid url"
    ]

)
def test_can_access_google_page(
        mocked_network_dependencies: tuple,
        has_connection: bool,
        valid_url: bool,
        result: str
) -> None:
    valid_google_url, has_internet_connection = mocked_network_dependencies

    valid_google_url.return_value = valid_url
    has_internet_connection.return_value = has_connection

    assert can_access_google_page("https://google.com") == result
