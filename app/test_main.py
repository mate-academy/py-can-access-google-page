import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize("url, valid_url_mock, internet_mock, expected", [
    ("https://www.google.com", True, True, "Accessible"),
    ("https://invalid.url", False, True, "Not accessible"),
    ("https://www.google.com", True, False, "Not accessible"),
    ("https://invalid.url", False, False, "Not accessible"),
])
def test_can_access_google_page(
        url: str,
        valid_url_mock: bool,
        internet_mock: bool,
        expected: str) -> None:
    with patch("app.main.valid_google_url", return_value=valid_url_mock), \
            patch("app.main.has_internet_connection",
                  return_value=internet_mock):
        result = can_access_google_page(url)
        assert result == expected
