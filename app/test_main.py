import pytest

from app.main import can_access_google_page
from unittest.mock import patch


@pytest.mark.parametrize(
    "internet_ok, url_ok, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(internet_ok, url_ok, expected):
    with patch("app.main.has_internet_connection") as mocked_internet, \
            patch("app.main.valid_google_url") as mocked_url:
        mocked_internet.return_value = internet_ok
        mocked_url.return_value = url_ok

        result = can_access_google_page("http://google.com")

        assert result == expected
