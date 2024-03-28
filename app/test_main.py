import pytest
from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "valid_google_url_return, has_internet_connection_return, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        mock_has_internet_connection: Callable,
        mock_valid_google_url: Callable,
        valid_google_url_return: bool,
        has_internet_connection_return: bool,
        expected_result: str
) -> None:
    mock_valid_google_url.return_value = valid_google_url_return
    mock_has_internet_connection.return_value = has_internet_connection_return
    assert can_access_google_page("") == expected_result
