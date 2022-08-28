from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_all_is_correct(google_url, time):
    google_url.return_value = True
    time.return_value = True
    assert can_access_google_page(google_url) == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_is_incorrect(google_url, time):
    google_url.return_value = False
    time.return_value = True
    assert can_access_google_page(google_url) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_time_is_incorrect(google_url, time):
    google_url.return_value = True
    time.return_value = False
    assert can_access_google_page(google_url) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_all_is_incorrect(google_url, time):
    google_url.return_value = False
    time.return_value = False
    assert can_access_google_page(google_url) == "Not accessible"
