from unittest import mock
from app.main import can_access_google_page
import pytest
from typing import Any


@pytest.mark.parametrize(
    "valid_url, connection, result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_with_various_conditions(
        mock_valid_url: Any,
        mock_internet_connection: Any,
        valid_url: bool,
        connection: bool,
        result: str,
) -> None:
    mock_valid_url.return_value = valid_url
    mock_internet_connection.return_value = connection
    assert can_access_google_page("url") == result
