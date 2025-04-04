import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, internet_available, expected_result",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", False, True, "Not accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://invalid-url.com", False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
    url: str,
    valid_url: bool,
    internet_available: bool,
    expected_result: str,
) -> None:
    with mock.patch("app.main.valid_google_url", return_value=valid_url), \
         mock.patch("app.main.has_internet_connection",
                    return_value=internet_available):
        result = can_access_google_page(url)
        assert result == expected_result
