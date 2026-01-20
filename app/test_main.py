from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_false_connection_false(mocked_valid, mocked_connectio):
    mocked_valid.return_value = False
    mocked_connectio.return_value = False
    assert can_access_google_page("http://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_true_connection_false(mocked_valid, mocked_connectio):
    mocked_valid.return_value = True
    mocked_connectio.return_value = False
    assert can_access_google_page("http://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_false_connection_true(mocked_valid, mocked_connectio):
    mocked_valid.return_value = False
    mocked_connectio.return_value = True
    assert can_access_google_page("http://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_true_connection_true(mocked_valid, mocked_connectio):
    mocked_valid.return_value = True
    mocked_connectio.return_value = True
    assert can_access_google_page("http://google.com") == "Accessible"
