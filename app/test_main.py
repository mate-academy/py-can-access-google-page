import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, internet_connection, valid_url, expected_result",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://google.com", False, True, "Not accessible"),
        ("https://invalidsite.com", True, False, "Not accessible"),
        ("https://invalidsite.com", False, False, "Not accessible"),
        ("", True, False, "Not accessible"),
    ],
)
def test_can_access_google_page(url: str, internet_connection: bool,
                                valid_url: bool, expected_result: str) -> None:
    with patch("app.main.has_internet_connection",
               return_value=internet_connection), \
         patch("app.main.valid_google_url", return_value=valid_url):
        result = can_access_google_page(url)
        assert result == expected_result
