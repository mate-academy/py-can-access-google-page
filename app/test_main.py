from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_true_connection_true(
        mocked_valid_google_url, mocked_has_internet_connection):
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com.ua") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_true_connection_false(
        mocked_valid_google_url, mocked_has_internet_connection):
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert \
        can_access_google_page("https://www.google.com.ua") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_false_connection_true(
        mocked_valid_google_url, mocked_has_internet_connection):
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert \
        can_access_google_page("https://www.google.com.ua") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_false_connection_false(
        mocked_valid_google_url, mocked_has_internet_connection):
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert \
        can_access_google_page("https://www.google.com.ua") == "Not accessible"
