import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, internet, valid, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", False, True, "Not accessible"),
        ("https://invalid-url.com", True, False, "Not accessible"),
        ("https://invalid-url.com", False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(url, internet, valid, expected):
    with patch("app.main.valid_google_url", return_value=valid), patch(
        "app.main.has_internet_connection", return_value=internet
    ):
        result = can_access_google_page(url)
        assert result == expected
