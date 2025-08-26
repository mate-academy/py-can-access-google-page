from app.main import can_access_google_page, valid_google_url, has_internet_connection
from unittest import mock


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_connecting_is_False(mocked_connection, mocked_url):
    mocked_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page(
        "https://github.com/Olexii-Babii/py-can-access-google-page") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_url_is_False(mocked_connection, mocked_url):
    mocked_url.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page(
        "https://github.com/Olexii-Babii/py-can-access-google-page") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_connecting_all_is_True(mocked_connection, mocked_url):
    mocked_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page(
        "https://github.com/Olexii-Babii/py-can-access-google-page") == "Accessible"
