import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_ok,url_ok,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        internet_ok: bool,
        url_ok: bool,
        expected: str
) -> None:
    with (patch("app.main.has_internet_connection", return_value=internet_ok),
          patch("app.main.valid_google_url", return_value=url_ok)):
        result = can_access_google_page("https://www.google.com")
        assert result == expected
