import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize("internet_connection, valid_url, expected_result", [
    (True, True, "Accessible"),
    (False, True, "Not accessible"),
    (True, False, "Not accessible"),
])
def test_can_access_google_page(internet_connection, valid_url, expected_result):
    with patch("app.main.has_internet_connection", return_value=internet_connection), \
         patch("app.main.valid_google_url", return_value=valid_url):
        result = can_access_google_page("https://www.google.com")
        assert result == expected_result
