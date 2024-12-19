from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_cannot_access_if_only_connection(mocked_connection, mocked_valid_url):
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_cannot_access_if_only_valid_url(mocked_connection, mocked_valid_url):
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_cannot_access_if_connection_and_url_invalid(mocked_connection, mocked_valid_url):
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_access_if_connection_and_valid_url(mocked_connection, mocked_valid_url):
    assert can_access_google_page("https://google.com") == "Accessible"



