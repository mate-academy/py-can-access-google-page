from unittest.mock import patch
from typing import Any
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "test_valid_link, test_has_internet_connection, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google(
        mock_valid_google_url: Any,
        mock_has_internet_connection: Any,
        test_valid_link: bool,
        test_has_internet_connection: bool,
        expected_result: str
) -> None:
    mock_valid_google_url.return_value = test_valid_link
    mock_has_internet_connection.return_value = test_has_internet_connection

    result = can_access_google_page("https://www.google.com")
    assert result == expected_result
