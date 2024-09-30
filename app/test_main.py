import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url_result, internet_connection_result, expected", [
        ("http://www.google.com", True, True, "Accessible"),
        ("http://www.invalid.com", False, True, "Not accessible"),
        ("http://www,google.com", True, False, "Not accessible")
    ],
    ids=[
        "Valid url and connection",
        "Invalid url and connection is ok",
        "Valid url, no internet"
    ]
)
def test_can_access_google_page(
        url: str,
        valid_url_result: bool,
        internet_connection_result: bool,
        expected: bool) -> None:
    with patch("app.main.valid_google_url") as mocked_valid_url, \
         patch("app.main.has_internet_connection") as mocked_connection:

        mocked_valid_url.return_value = valid_url_result
        mocked_connection.return_value = internet_connection_result

        assert can_access_google_page(url) == expected
