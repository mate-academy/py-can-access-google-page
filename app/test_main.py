from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_no_access_with_no_internet(mocked_url, mocked_connection):
    mocked_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page("whatever") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_no_access_with_non_valid_url(mocked_url, mocked_connection):
    mocked_url.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page("whatever") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_return_access(mocked_url, mocked_connection):
    mocked_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page("whatever") == "Accessible"
