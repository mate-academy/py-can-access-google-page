from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cannot_access_if_only_valid_google_url(
        mocked_url, mocked_connection):
    mocked_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page("www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cannot_access_if_only_has_internet_connection(
        mocked_url, mocked_connection):
    mocked_url.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page("www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cannot_access_if_not_valid_google_url_no_internet_connection(
        mocked_url, mocked_connection):
    mocked_url.return_value = False
    mocked_connection.return_value = False
    assert can_access_google_page("www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_if_valid_google_url_and_has_internet_connection(
        mocked_url, mocked_connection):
    mocked_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page("www.google.com") == "Accessible"
