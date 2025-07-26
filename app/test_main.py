from unittest import mock
from typing import Any
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_connection, valid_url, expected_result, should_call_url",
    [
        (True, True, "Accessible", True),
        (True, False, "Not accessible", True),
        (False, True, "Not accessible", False),
        (False, False, "Not accessible", False),
    ],
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_parametrized(
    mock_connection: Any, mock_url: Any,
    has_connection: bool, valid_url: bool,
    expected_result: str, should_call_url: bool
) -> None:
    mock_connection.return_value = has_connection
    mock_url.return_value = valid_url

    result = can_access_google_page("url")

    assert result == expected_result

    if should_call_url:
        mock_url.assert_called_once_with("url")
    else:
        mock_url.assert_not_called()
