import pytest
from unittest import mock

import app.main
from app.main import can_access_google_page

@pytest.mark.parametrize(
    "url,can_connect,valid_url,result",
    [
        ("http://www.google.pl", True, True, "Accessible"),
        ("http://www.google.pl", False, True, "Not accessible"),
        ("my_url", True, False, "Not accessible"),
        ("my_url", False, False, "Not accessible"),
    ]
)

def test_can_access_google_page(url, can_connect, valid_url, result):
    with (mock.patch("app.main.has_internet_connection") as mock_internet_connection,
          mock.patch("app.main.valid_google_url") as mock_valid_google_url):
        mock_internet_connection.return_value = can_connect
        mock_valid_google_url.return_value = valid_url
        assert can_access_google_page("http://www.google.pl") == result