import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_valid, connection_active, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(url_valid, connection_active, expected):
    with patch("app.main.valid_google_url") as mock_url, \
            patch("app.main.has_internet_connection") as mock_conn:
        mock_url.return_value = url_valid
        mock_conn.return_value = connection_active

        result = can_access_google_page("https://www.google.com")
        assert result == expected
