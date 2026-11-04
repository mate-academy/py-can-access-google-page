from unittest.mock import patch
from typing import Any
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet, is_valid_url, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_google_url(mock_valid_google_url: Any ,
                          mock_has_internet_connection: Any,
                          has_internet: bool,
                          is_valid_url: bool,
                          expected_result: str) -> None:
    mock_valid_google_url.return_value = is_valid_url
    mock_has_internet_connection.return_value = has_internet

    dummy_url = "https://www.google.com"
    result = can_access_google_page(dummy_url)

    assert result == expected_result

    mock_has_internet_connection.assert_called_once()
    if has_internet:
        mock_valid_google_url.assert_called_once_with(
            dummy_url
        )
