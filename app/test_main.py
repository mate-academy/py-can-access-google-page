import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, has_internet, excepted",
    [
        ("http://www.google.com", True, True, "Accessible"),
        ("http://www.google.com", True, False, "Not accessible"),
        ("http://www.invalid_url.com", False, True, "Not accessible"),
        ("http://www.invalid_url.com", False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        url: str,
        valid_url: bool,
        has_internet: bool,
        excepted: str
) -> None:
    with mock.patch("app.main.valid_google_url", return_value=valid_url), \
            mock.patch("app.main.has_internet_connection",
                       return_value=has_internet):
        assert can_access_google_page(url) == excepted
