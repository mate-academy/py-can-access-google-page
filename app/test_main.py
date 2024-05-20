import pytest
from unittest.mock import patch
from app.main import can_access_google_page

test_data = [
    (True, True, "http://www.google.com", "Accessible"),
    (False, True, "http://www.google.com", "Not accessible"),
    (True, False, "http://www.google.com", "Not accessible"),
    (False, False, "http://www.google.com", "Not accessible")
]


@pytest.mark.parametrize(
    "internet_connection, valid_url, url, expected", test_data)
def test_can_access_google_page(
        internet_connection: bool, valid_url: bool, url: str, expected: str)\
        -> None:
    with patch("app.main.has_internet_connection", return_value=internet_connection):  # noqa: E501
        with patch("app.main.valid_google_url", return_value=valid_url):
            assert can_access_google_page(url) == expected
