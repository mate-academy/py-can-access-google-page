import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, is_valid_url, has_connection, expected", [
        ("https://google.com", True, True, "Accessible"),
        ("https://google.com", True, False, "Not accessible"),
        ("https://notgoogle.com", False, True, "Not accessible"),
        ("https://notgoogle.com", False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        url: str,
        is_valid_url: bool,
        has_connection: bool,
        expected: str
) -> None:
    with patch(
            "app.main.valid_google_url",
            return_value=is_valid_url), \
         patch(
             "app.main.has_internet_connection",
             return_value=has_connection):
        result = can_access_google_page(url)
        assert result == expected, (
            f"\nExpected: {expected}"
            f"\nGot: {result}"
            f"\nInput: url={url}, "
            f"valid_google_url={is_valid_url}, "
            f"has_internet_connection={has_connection}"
        )
