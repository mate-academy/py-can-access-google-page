from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_connection_is_on_and_url_is_correct(
        mocked_valid_google_url,
        mocked_internet_connection
):
    mocked_valid_google_url.return_value = True
    mocked_internet_connection.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_connection_is_on_and_url_is_incorrect(
        mocked_valid_google_url,
        mocked_internet_connection
):
    mocked_valid_google_url.return_value = False
    mocked_internet_connection.return_value = True

    assert can_access_google_page("https://asdaasdas.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_connection_is_off_and_url_is_correct(
        mocked_valid_google_url,
        mocked_internet_connection
):
    mocked_valid_google_url.return_value = True
    mocked_internet_connection.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_connection_is_off_and_url_is_incorrect(
        mocked_valid_google_url,
        mocked_internet_connection
):
    mocked_valid_google_url.return_value = False
    mocked_internet_connection.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"
