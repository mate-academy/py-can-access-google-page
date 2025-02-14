from unittest.mock import patch
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,has_connection,is_valid,expected",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://google.com", False, True, "Not accessible"),
        ("https://google.com", True, False, "Not accessible"),
        ("https://google.com", False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        url: str,
        has_connection: bool,
        is_valid: bool,
        expected: str
) -> None:

    with (
        patch("app.main.has_internet_connection", return_value=has_connection),
        patch("app.main.valid_google_url", return_value=is_valid)
    ):
        result = can_access_google_page(url)
        assert result == expected
