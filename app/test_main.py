from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, has_internet, is_valid, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", False, True, "Not accessible"),
        ("https://somewebsitename.com", True, False, "Not accessible"),
        ("https://somewebsitename.com", False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
    url: str, has_internet: bool, is_valid: bool, expected: str
) -> None:
    with mock.patch("app.main.has_internet_connection", return_value=has_internet):
        with mock.patch("app.main.valid_google_url", return_value=is_valid):
            assert can_access_google_page(url) == expected
