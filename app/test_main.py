import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_status, url_status, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "valid_url_and_connection_exists",
        "invalid_url_but_connection_exists",
        "valid_url_but_no_connection",
        "invalid_url_and_no_connection",
    ]
)
def test_can_access_google_page(internet_status: bool,
                                url_status: bool, expected: str) -> None:
    with patch("app.main.has_internet_connection", return_value=internet_status), \
         patch("app.main.valid_google_url", return_value=url_status):
        assert can_access_google_page("http://www.google.com") == expected
