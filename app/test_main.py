from unittest.mock import patch
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet, url_valid, expected_access",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(internet: bool, url_valid: bool,
                                expected_access: str) -> None:
    with patch("app.main.has_internet_connection", return_value=internet), \
         patch("app.main.valid_google_url", return_value=url_valid):
        assert can_access_google_page("https://www.google.com"
                                      ) == expected_access
