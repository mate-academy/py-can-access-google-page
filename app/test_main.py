from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mocked_url: bool, mocked_connection: bool) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page("https://www.google.com/") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_valid_url_and_no_connection(
        mocked_url: bool, mocked_connection: bool) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = False
    assert (can_access_google_page("https://www.google.com/")
            == "Not accessible")


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_no_connection(
        mocked_url: bool, mocked_connection: bool) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = False
    assert (can_access_google_page("https://www.google.com/")
            == "Not accessible")


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_valid_url_and_connection_exists(
        mocked_url: bool, mocked_connection: bool) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = True
    assert (can_access_google_page("https://www.google.com/")
            == "Not accessible")
