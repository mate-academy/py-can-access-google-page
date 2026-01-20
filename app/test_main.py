from unittest.mock import patch
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize("has_internet,valid_url,expected_result", [
    (True, True, "Accessible"),
    (False, True, "Not accessible"),
    (True, False, "Not accessible"),
    (False, False, "Not accessible")
])
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        has_internet_connextion_mock: bool,
        valid_google_url_mock: bool,
        has_internet: str,
        valid_url: str,
        expected_result: list
) -> list:
    url = "https://www.google.com"
    has_internet_connextion_mock.return_value = has_internet
    valid_google_url_mock.return_value = valid_url
    result = can_access_google_page(url)
    assert result == expected_result
