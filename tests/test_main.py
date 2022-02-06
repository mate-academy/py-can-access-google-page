from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_success_access_page(mocked_valid_google_url,
                             mocked_internet_connection):

    mocked_valid_google_url.return_value = True
    mocked_internet_connection.return_value = True
    assert can_access_google_page("") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_access_google_page(mocked_valid_google_url,
                                mocked_internet_connection):
    mocked_valid_google_url.return_value = True
    mocked_internet_connection.return_value = False
    assert can_access_google_page("") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cant_visit_google_page(mocked_valid_google_url,
                                mocked_internet_connection):

    mocked_valid_google_url.return_value = False
    mocked_internet_connection.return_value = True

    assert can_access_google_page("") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_havent_access_to_google_page(mocked_valid_google_url,
                                      mocked_internet_connection):

    mocked_valid_google_url.return_value = False
    mocked_internet_connection.return_value = False

    assert can_access_google_page("") == "Not accessible"
