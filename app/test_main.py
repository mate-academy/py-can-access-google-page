from app.main import can_access_google_page
from unittest.mock import patch
import pytest


@pytest.mark.parametrize(
    "is_valid_url, has_connection, expected",
    [
        (True, True, "Accessible"),  # Допустимый URL и есть интернет
        (True, False, "Not accessible"),  # Допустимый URL, но нет интернета
        (False, True, "Not accessible"),  # Недопустимый URL, даже если инте
        (False, False, "Not accessible"),  # Недопустимый URL и нет интернета
    ],
)
def test_can_access_google_page(
    is_valid_url: bool, has_connection: bool, expected: str
) -> None:
    with patch("app.main.valid_google_url", return_value=is_valid_url), \
         patch("app.main.has_internet_connection",
               return_value=has_connection):

        result = can_access_google_page("https://www.google.com")
        assert result == expected, f"Expected '{expected}' but got '{result}'"
