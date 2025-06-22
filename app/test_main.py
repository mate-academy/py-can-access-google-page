from unittest import mock
import app.main
import datetime
import requests


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_url, mocked_connection):
    mocked_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"
