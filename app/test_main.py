import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, has_internet, expected",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://invalid.com", False, True, "Not accessible"),
        ("https://google.com", True, False, "Not accessible"),
        ("https://invalid.com", False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    url: str,
    valid_url: bool,
    has_internet: bool,
    expected: str,
) -> None:
    with patch("app.main.valid_google_url", return_value=valid_url):
        with patch(
            "app.main.has_internet_connection", return_value=has_internet
        ):
            result = can_access_google_page(url)
            assert result == expected
