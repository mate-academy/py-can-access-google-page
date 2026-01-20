import pytest
from unittest.mock import patch
from app.main import can_access_google_page
from typing import Any


@pytest.mark.parametrize("internet_connection, valid_url, expected_result", [
    (True, True, "Accessible"),
    (False, True, "Not accessible"),
    (True, False, "Not accessible"),
    (False, False, "Not accessible"),
], ids=[
    "Internet Available & Valid URL",
    "Internet Not Available",
    "Internet Available & Invalid URL",
    "Internet Not Available & Invalid URL"
])
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: Any,
        mock_valid_google_url: Any,
        internet_connection: bool,
        valid_url: bool,
        expected_result: str
) -> None:
    mock_has_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = valid_url
    assert can_access_google_page("https://www.google.com") == expected_result
