from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_valid_google_url(
        mocked_url, mocked_connection):
    mocked_url.return_value = False
    mocked_connection.return_value = True
    test = can_access_google_page(
        "https//developer.mozilla.org")
    assert test == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_google_url_and_has_internet(
        mocked_url, mocked_connection):
    mocked_url.return_value = True
    mocked_connection.return_value = True
    test = can_access_google_page(
        "https://developer.mozilla.org")
    assert test == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_valid_url_not_has_internet_connection(
        mocked_url, mocked_connection):
    mocked_url.return_value = False
    mocked_connection.return_value = False
    test = can_access_google_page(
        "https:/developer.mozilla.org")
    assert test == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_google_url_and_has_internet(
        mocked_url, mocked_connection):
    mocked_url.return_value = True
    mocked_connection.return_value = False
    test = can_access_google_page(
        "https://developer.mozilla.org")
    assert test == "Not accessible"
