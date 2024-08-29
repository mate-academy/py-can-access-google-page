import pytest
from typing import Any
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url_return, "
    "has_internet_connection_return,"
    "result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        valid_google_url_mock: Any,
        has_internet_connection_mock: Any,
        valid_google_url_return: bool,
        has_internet_connection_return: bool,
        result: str
) -> None:
    valid_google_url_mock.return_value = valid_google_url_return
    has_internet_connection_mock.return_value = has_internet_connection_return
    assert can_access_google_page("example.org") == result

    has_internet_connection_mock.assert_called_once()
    if has_internet_connection_mock.return_value:
        valid_google_url_mock.assert_called_once()
