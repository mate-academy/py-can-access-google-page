from app.main import can_access_google_page
from unittest import mock


@mock.patch('app.main.has_internet_connection')
@mock.patch('app.main.valid_google_url')
def test_connection_and_url_are_good(google_url, connection):
    google_url.return_value = True
    connection.return_value = True
    assert can_access_google_page('google.com') == "Accessible"


@mock.patch('app.main.has_internet_connection')
@mock.patch('app.main.valid_google_url')
def test_valid_page_no_interntet_connection(google_url, connection):
    google_url.return_value = True
    connection.return_value = False
    assert can_access_google_page('google.com') == "Not accessible"


@mock.patch('app.main.has_internet_connection')
@mock.patch('app.main.valid_google_url')
def test_bad_url(google_url, connection):
    google_url.return_value = False
    connection.return_value = True
    assert can_access_google_page('google.com') == "Not accessible"
