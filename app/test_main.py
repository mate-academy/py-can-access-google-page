from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_and_connection_are_valid(
        mocked_google_url: bool,
        mocked_internet_connection: bool
) -> None:
    mocked_google_url.return_value = True
    mocked_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_and_connection_are_invalid(
        mocked_google_url: bool,
        mocked_internet_connection: bool
) -> None:
    mocked_google_url.return_value = False
    mocked_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_valid_and_connection_invalid(
        mocked_google_url: bool,
        mocked_internet_connection: bool
) -> None:
    mocked_google_url.return_value = True
    mocked_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_invalid_and_connection_valid(
        mocked_google_url: bool,
        mocked_internet_connection: bool
) -> None:
    mocked_google_url.return_value = False
    mocked_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"
