from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(
        mocked_valid_url: bool,
        mocked_has_connection: bool
) -> None:
    mocked_valid_url.return_value = True
    mocked_has_connection.return_value = True
    assert can_access_google_page("https://www.google.com.ua/") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_for_incorrect_url(
        mocked_valid_url: bool,
        mocked_has_connection: bool
) -> None:
    mocked_valid_url.return_value = False
    mocked_has_connection.return_value = True
    assert can_access_google_page("incorrect_url") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_has_no_internet_connection(
        mocked_valid_url: bool,
        mocked_has_connection: bool
) -> None:
    mocked_valid_url.return_value = True
    mocked_has_connection.return_value = False
    assert can_access_google_page("incorrect_url") == "Not accessible"
