import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, mock_valid_url, mock_internet, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://invalid-url.com", False, True, "Not accessible"),
        ("https://invalid-url.com", False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(url: str,
                                mock_valid_url: bool,
                                mock_internet: bool,
                                expected: str) -> None:
    with (patch("app.main.valid_google_url", return_value=mock_valid_url),
          patch("app.main.has_internet_connection",
                return_value=mock_internet)):
        assert can_access_google_page(url) == expected
