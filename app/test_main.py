import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize("mock_valid_url, mock_internet, expected", [
    (True, True, "Accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (False, False, "Not accessible"),
])
def test_can_access_google_page(mock_valid_url: bool, mock_internet: bool, expected: str) -> None:
    with patch("app.main.valid_google_url", return_value=mock_valid_url), \
         patch("app.main.has_internet_connection", return_value=mock_internet):
        assert can_access_google_page("https://www.google.com") == expected
