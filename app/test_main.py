import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_available, valid_url, expected", [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ])
def test_can_access_google_page(
        internet_available: bool,
        valid_url: bool,
        expected: str
) -> None:
    with patch("app.main.has_internet_connection",
               return_value=internet_available):
        with patch("app.main.valid_google_url",
                   return_value=valid_url):
            assert can_access_google_page(
                "https://www.google.com"
            ) == expected
