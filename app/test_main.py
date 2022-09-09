from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_google_page_accessible(mocked_url, mocked_internet):
    mocked_url.return_value = True
    mocked_internet.return_value = True
    result = can_access_google_page(url="https://www.google.com.ua")
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_google_page_no_access_when_url_is_false(mocked_url, mocked_internet):
    mocked_url.return_value = False
    mocked_internet.return_value = True
    result = can_access_google_page(url="https://www.google.com.ua")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_google_page_no_access_when_no_internet(mocked_url, mocked_internet):
    mocked_url.return_value = True
    mocked_internet.return_value = False
    result = can_access_google_page(url="https://www.google.com.ua")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_google_page_no_access_no_url_no_internet(mocked_url, mocked_internet):
    mocked_url.return_value = False
    mocked_internet.return_value = False
    result = can_access_google_page(url="https://www.google.com.ua")
    assert result == "Not accessible"
