import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url_result, internet_result, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://fake-url.com", False, True, "Not accessible"),
        ("https://fake-url.com", False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    url: str, valid_url_result: bool, internet_result: bool,
    expected: str,
) -> None:
    with patch("app.main.valid_google_url", return_value=valid_url_result), \
         patch("app.main.has_internet_connection",
               return_value=internet_result):
        assert can_access_google_page(url) == expected
