from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_connection(mocked_int_connection, mocked_valid_url):
    mocked_int_connection.return_value = True
    mocked_valid_url.return_value = True
    assert can_access_google_page("http://google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_connection_but_invalid_url(mocked_int_connection, mocked_valid_url):
    mocked_int_connection.return_value = True
    mocked_valid_url.return_value = False
    assert can_access_google_page("http://wrongeurl.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_but_no_connection(mocked_int_connection, mocked_valid_url):
    mocked_int_connection.return_value = False
    mocked_valid_url.return_value = True
    assert can_access_google_page("http://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_invalid_url_and_no_connection(mocked_int_connection, mocked_valid_url):
    mocked_int_connection.return_value = False
    mocked_valid_url.return_value = False
    assert can_access_google_page("http://wrongeurl.com") == "Not accessible"
