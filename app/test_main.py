from app import main
from unittest import mock
import pytest

URL = [
    (True, True, "Accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (False, False, "Not accessible"),
]


@pytest.mark.parametrize("inet_ok, url_ok, expected", URL)
def test_can_access_google_page(inet_ok: bool, url_ok: bool, expected: str) -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid, \
        mock.patch("app.main.has_internet_connection") as mock_conn:
        mock_valid.return_value = url_ok
        mock_conn.return_value = inet_ok
        result = main.can_access_google_page("https://google.com")
        assert result == expected
