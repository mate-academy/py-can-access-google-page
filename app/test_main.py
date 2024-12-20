import pytest
from unittest.mock import patch
from app.main import can_access_google_page

@pytest.mark.parametrize(
    "valid_url, has_connection, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(valid_url, has_connection, expected):
    with patch("app.main.valid_google_url", return_value=valid_url):
        with patch("app.main.has_internet_connection", return_value=has_connection):
            result = can_access_google_page("https://test-url.com")
            assert result == expected, f"Expected '{expected}' but got '{result}'."
