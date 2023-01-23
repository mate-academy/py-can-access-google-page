from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_google_url_and_has_internet_connection(
        mocked_valid_google_url: str,
        mocked_has_internet_connection: str
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com/") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_google_url_and_has_no_internet_connection(
        mocked_valid_google_url: str,
        mocked_has_internet_connection: str
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com/") \
           == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_google_url_and_has_internet_connection(
        mocked_valid_google_url: str,
        mocked_has_internet_connection: str
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com/") \
           == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_google_url_and_has_no_internet_connection(
        mocked_valid_google_url: str,
        mocked_has_internet_connection: str
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com/") \
           == "Not accessible"
