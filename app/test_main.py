import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize("url, valid_url, internet, expected", [
    ("https://www.google.com", True, True, "Accessible"),
    ("https://www.google.com", True, False, "Not accessible"),
    ("https://www.fakegoogle.com", False, True, "Not accessible"),
    ("https://www.fakegoogle.com", False, False, "Not accessible")
])
def test_can_access_google_page(url: str,
                                valid_url: bool,
                                internet: bool,
                                expected: str) -> None:
    with patch("app.main.valid_google_url", return_value=valid_url), \
         patch("app.main.has_internet_connection", return_value=internet):
        result = can_access_google_page(url)
        assert result == expected
