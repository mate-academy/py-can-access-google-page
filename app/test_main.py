import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, has_connection, expected_output", [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ])
def test_can_access_google_page(
        is_valid_url: str,
        has_connection: bool,
        expected_output: str
) -> None:
    with patch("app.main.valid_google_url", return_value=is_valid_url), \
            patch(
                "app.main.has_internet_connection",
                return_value=has_connection):
        assert can_access_google_page(
            "http://www.google.com"
        ) == expected_output
