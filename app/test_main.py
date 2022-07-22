from unittest import mock
from app.main import can_access_google_page


@mock.patch('app.main.has_internet_connection')
@mock.patch('app.main.valid_google_url')
def test_not_connection(google_url, connection):
    google_url.return_value, connection.return_value = True, False
    assert can_access_google_page('google.com') == "Not accessible"


@mock.patch('app.main.has_internet_connection')
@mock.patch('app.main.valid_google_url')
def test_wrong_url(google_url, connection):
    google_url.return_value, connection.return_value = False, True
    assert can_access_google_page('google.com') == "Not accessible"


@mock.patch('app.main.has_internet_connection')
@mock.patch('app.main.valid_google_url')
def test_connection_correct_url(google_url, connection):
    google_url.return_value, connection.return_value = True, True
    assert can_access_google_page('google.com') == "Accessible"
