from app.main import can_access_google_page
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "url,val_url,internet,expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://www.badsite.com", False, True, "Not accessible"),
        ("https://www.badsite.com", False, False, "Not accessible"),
    ],
)
def test_valid_url_and_internet_connection(
        url: str,
        val_url: bool,
        internet: bool,
        expected: str
) -> None:
    with mock.patch("app.main.valid_google_url", return_value=val_url), \
        mock.patch("app.main.has_internet_connection",
                   return_value=internet):
        result = can_access_google_page(url)
    assert result == expected
