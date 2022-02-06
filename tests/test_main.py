from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_has_connection_and_valid_url(mocked_internet_connection_connection,
                                      mocked_valid_url):
    mocked_internet_connection_connection.return_value = True
    mocked_valid_url.return_value = True

    assert can_access_google_page("http://google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_no_connection_and_invalid_url(mocked_internet_connection,
                                       mocked_valid_url):
    mocked_internet_connection.return_value = False
    mocked_valid_url.return_value = False

    assert can_access_google_page("http://fakegoogle.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_no_connection_and_valid_url(mocked_internet_connection,
                                     mocked_valid_url):
    mocked_internet_connection.return_value = False
    mocked_valid_url.return_value = True

    assert can_access_google_page("http://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_has_connection_and_invalid_url(mocked_internet_connection,
                                        mocked_valid_url):
    mocked_internet_connection.return_value = True
    mocked_valid_url.return_value = False

    assert can_access_google_page("http://iamgoogle.com") == "Not accessible"
