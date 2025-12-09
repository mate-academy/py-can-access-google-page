import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, has_internet, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(is_valid_url: bool,
                                has_internet: bool, expected: str) -> None:
    """Test can_access_google_page with mocked dependencies."""

    with patch("app.main.valid_google_url", return_value=is_valid_url):
        with patch("app.main.has_internet_connection",
                   return_value=has_internet):
            result = can_access_google_page("https://google.com")
            assert result == expected
