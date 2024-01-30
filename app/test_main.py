import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, is_valid_url, has_connection, expected_output", [
        ("http://www.google.com", True, True, "Accessible"),
        ("http://www.google.com", False, True, "Not accessible"),
        ("http://www.google.com", True, False, "Not accessible"),
        ("http://www.google.com", False, False, "Not accessible"),
        ("http://www.someotherwebsite.com", False, True, "Not accessible"),
    ])
def test_can_access_google_page(
        url: str,
        is_valid_url: str,
        has_connection: bool,
        expected_output: str
) -> None:
    with patch("app.main.valid_google_url", return_value=is_valid_url), \
            patch(
                "app.main.has_internet_connection",
                return_value=has_connection):

        assert can_access_google_page(url) == expected_output
