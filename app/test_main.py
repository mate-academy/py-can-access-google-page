from pytest import mark
from typing import Callable
from unittest import mock

from app.main import can_access_google_page


@mark.parametrize(
    "url_validation, connection_validation, url, accessibility",
    [
        (True, True, "mate.academy", "Accessible"),
        (True, False, "mate.academy", "Not accessible"),
        (False, True, "bro.academy", "Not accessible")
    ],
    ids=[
        "test when valid url and connection exists",
        "test when valid url but no connection",
        "test when connection exists but url invalid"
    ]
)
@mock.patch(
    "app.main.valid_google_url"
)
@mock.patch(
    "app.main.has_internet_connection"
)
def test_access_with_different_urls_and_internet_connection(
        mocked_url: Callable[[str], bool],
        mocked_connection: Callable[[], bool],
        url_validation: str,
        connection_validation: str,
        url: str,
        accessibility: str
) -> None:
    mocked_url.return_value = url_validation
    mocked_connection.return_value = connection_validation
    assert can_access_google_page(url) == accessibility
