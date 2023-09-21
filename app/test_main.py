import datetime
from unittest import mock

import requests
from .main import *


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_time_and_url(internet, google_valid):
    internet.return_value = True
    google_valid.return_value = True
    assert can_access_google_page("https://www.google.com/") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_invalid_time_valid_url(internet, google_valid):
    internet.return_value = False
    google_valid.return_value = True
    assert can_access_google_page("https://www.google.com/") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_time_invalid_url(internet, google_valid):
    internet.return_value = True
    google_valid.return_value = False
    assert can_access_google_page("https://www.google.com/") == "Not accessible"
