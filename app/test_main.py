import pytest
from unittest.mock import patch
import app.main as main


@pytest.mark.parametrize("internet, valid_url, expected", [
    (True, True, "Accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (False, False, "Not accessible"),
])
def test_can_access_google_page(internet: bool,
                                valid_url: bool, expected: str) -> None:
    with patch("app.main.has_internet_connection", return_value=internet), \
         patch("app.main.valid_google_url", return_value=valid_url):
        result = main.can_access_google_page("https://www.google.com")
    assert result == expected
