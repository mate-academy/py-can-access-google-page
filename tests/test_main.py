from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_connection_and_valid_url(
        mocked_valid_google_url,
        mocked_internet_connection
):
    mocked_valid_google_url.return_value = True
    mocked_internet_connection.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_no_connection_and_valid_url(
        mocked_valid_google_url,
        mocked_has_internet_connection
):
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False

    assert can_access_google_page("http://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_connection_and_invalid_url(
        mocked_valid_google_url,
        mocked_internet_connection
):
    mocked_valid_google_url.return_value = False
    mocked_internet_connection.return_value = True

    assert can_access_google_page("https://fsfsdgle.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_no_connection_and_invalid_url(
        mocked_valid_google_url,
        mocked_internet_connection
):
    mocked_valid_google_url.return_value = False
    mocked_internet_connection.return_value = False

    assert can_access_google_page("https://gsdgle.com") == "Not accessible"
