import pytest
from unittest.mock import patch
from app.main import can_access_google_page


GOOGLE_URL = "https://www.google.com"
INVALID_URL = "https://www.invalidurl.com"


@pytest.mark.parametrize(
    "url, valid_url, has_internet, expected",
    [
        (GOOGLE_URL, True, True, "Accessible"),
        (GOOGLE_URL, True, False, "Not accessible"),
        (INVALID_URL, False, True, "Not accessible"),
        (INVALID_URL, False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
    url: str,
        valid_url: bool,
        has_internet: bool,
        expected: str
) -> None:
    with patch("app.main.valid_google_url", return_value=valid_url):
        with patch(
                "app.main.has_internet_connection", return_value=has_internet
        ):
            assert can_access_google_page(url) == expected, (
                f"Failed for URL: {url}, valid_url: {valid_url}, "
                f"has_internet: {has_internet}"
            )
