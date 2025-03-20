from app.main import can_access_google_page
import pytest
from unittest.mock import patch


@pytest.mark.parametrize(
    "url, valid_url, has_connection, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("invalid_url", False, True, "Not accessible"),
        ("invalid_url", False, False, "Not accessible"),
    ]
)
def test_valid_url_and_connection_exists(
        url: str,
        valid_url: bool,
        has_connection: bool,
        expected: str
) -> None:
    with patch("app.main.valid_google_url", return_value=valid_url), \
         patch(
             "app.main.has_internet_connection",
               return_value=has_connection):
        assert can_access_google_page(url) == expected
