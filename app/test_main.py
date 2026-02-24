import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, is_valid, has_internet, expected",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://google.com", True, False, "Not accessible"),
        ("https://example.com", False, True, "Not accessible"),
        ("https://example.com", False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    url: str,
    is_valid: bool,
    has_internet: bool,
    expected: str,
) -> None:
    with patch("app.main.valid_google_url") as mock_valid, \
         patch("app.main.has_internet_connection") as mock_internet:

        mock_valid.return_value = is_valid
        mock_internet.return_value = has_internet

        result = can_access_google_page(url)

        assert result == expected