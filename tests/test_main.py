from unittest import mock
from app.main import can_access_google_page, valid_google_url, has_internet_connection


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_true_connection_true(internet_connection, valid_url):
    internet_connection.return_value = True
    valid_url.return_value = True
    assert can_access_google_page("https://www.google.com.ua/") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_false_connection_false(internet_connection, valid_url):
    internet_connection.return_value = False
    valid_url.return_value = False
    assert can_access_google_page("https://www.google.com.ua/") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_true_connection_false(internet_connection, valid_url):
    internet_connection.return_value = True
    valid_url.return_value = False
    assert can_access_google_page("https://www.google.com.ua/") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_false_connection_true(internet_connection, valid_url):
    internet_connection.return_value = False
    valid_url.return_value = True
    assert can_access_google_page("https://www.google.com.ua/") == "Not accessible"
