from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, url_valid, internet_connect, expected",
    [
        ("https://google.com", False, True, "Not accessible"),
        ("https://google.com", True, True, "Accessible"),
        ("bad_url_address", True, False, "Not accessible"),
        ("bad_url_address", False, False, "Not accessible")
    ]
)
def test_can_access_google_page_accessible(
        url: str,
        url_valid: bool,
        internet_connect: bool,
        expected: str
) -> None:
    with mock.patch("app.main.valid_google_url") as google_url, \
         mock.patch("app.main.has_internet_connection") as internet_connection:

        google_url.return_value = url_valid
        internet_connection.return_value = internet_connect

        result = can_access_google_page(url)

        assert result == expected
