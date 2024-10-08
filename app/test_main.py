# app/test_main.py
from app.main import can_access_google_page
import pytest
from unittest.mock import patch


@pytest.mark.parametrize(
    "url, valid_url, has_internet, expected_result",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("invalid_url", False, True, "Not accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("invalid_url", False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        url: str,
        valid_url: bool,
        has_internet: bool,
        expected_result: str
) -> None:
    with patch("app.main.valid_google_url", return_value=valid_url):
        with patch(
                "app.main.has_internet_connection", return_value=has_internet
        ):
            result = can_access_google_page(url)
            assert result == expected_result
