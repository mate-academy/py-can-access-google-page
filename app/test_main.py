from unittest import mock

from app.main import can_access_google_page


@mock.patch('app.main.has_internet_connection')
@mock.patch('app.main.valid_google_url')
def test_incorrect_url(google_url, connection):
    google_url.return_value, connection.return_value = False, True
    assert can_access_google_page('google.com') == "Not accessible"


@mock.patch('app.main.has_internet_connection')
@mock.patch('app.main.valid_google_url')
def test_dont_have_internet_connection(google_url, connection):
    google_url.return_value, connection.return_value = True, False
    assert can_access_google_page('google.com') == "Not accessible"


@mock.patch('app.main.has_internet_connection')
@mock.patch('app.main.valid_google_url')
def test_have_connection_and_correct_url(google_url, connection):
    google_url.return_value, connection.return_value = True, True
    assert can_access_google_page('google.com') == "Accessible"
