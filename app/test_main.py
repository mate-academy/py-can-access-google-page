from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_is_invalid_and_has_connection(mocked_url, mocked_cnnection):
    mocked_url.return_value = False
    mocked_cnnection.return_value = True
    assert can_access_google_page(200) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_is_valid_and_has_no_connection(mocked_url, mocked_cnnection):
    mocked_url.return_value = True
    mocked_cnnection.return_value = False
    assert can_access_google_page(200) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_is_valid_and_has_connection(mocked_url, mocked_cnnection):
    mocked_url.return_value = True
    mocked_cnnection.return_value = True
    assert can_access_google_page(200) == "Accessible"
