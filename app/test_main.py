from app.main import can_access_google_page
from unittest import mock


@mock.patch('app.main.valid_google_url')
@mock.patch('app.main.has_internet_connection')
def test_return_access_passed(
        mocked_valid_google_url,
        mocked_has_internet_connect
):
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connect.return_value = True
    assert can_access_google_page("https://www.google.com/") ==\
           "Accessible"


@mock.patch('app.main.valid_google_url')
@mock.patch('app.main.has_internet_connection')
def test_return_access_denied_if_url_wrong(
        mocked_valid_google_url,
        mocked_has_internet_connect
):
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connect.return_value = True
    assert can_access_google_page("https://www.google.com/") ==\
           "Not accessible"


@mock.patch('app.main.valid_google_url')
@mock.patch('app.main.has_internet_connection')
def test_return_access_denied_if_time_is_wrong(
        mocked_valid_google_url,
        mocked_has_internet_connect
):
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connect.return_value = False
    assert can_access_google_page("https://www.google.com/") ==\
           "Not accessible"


@mock.patch('app.main.valid_google_url')
@mock.patch('app.main.has_internet_connection')
def test_return_access_denied_if_time_and_url_wrong(
        mocked_valid_google_url,
        mocked_has_internet_connect
):
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connect.return_value = False
    assert can_access_google_page("https://www.google.com/") ==\
           "Not accessible"
