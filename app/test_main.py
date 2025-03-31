import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
        valid_url: bool, internet: bool, expected: str
) -> None:
    with patch("app.main.valid_google_url", return_value=valid_url), \
         patch("app.main.has_internet_connection", return_value=internet):

        result = can_access_google_page("https://www.google.com")
        assert result == expected
