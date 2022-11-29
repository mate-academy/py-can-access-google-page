from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_url_and_connection_are_valid(
        mocked_valid_url: bool,
        mocked_internet_connection: bool
) -> None:
    mocked_valid_url.return_value = True
    mocked_internet_connection.return_value = True
    assert can_access_google_page("https://mate.academy") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_url_and_connection_are_not_valid(
        mocked_valid_url: bool,
        mocked_internet_connection: bool
) -> None:
    mocked_valid_url.return_value = False
    mocked_internet_connection.return_value = False
    assert can_access_google_page("https://mate.academy") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_url_is_not_valid(
        mocked_valid_url: bool,
        mocked_internet_connection: bool
) -> None:
    mocked_valid_url.return_value = False
    mocked_internet_connection.return_value = True
    assert can_access_google_page("https://mate.academy") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_there_is_no_internet_connection(
        mocked_valid_url: bool,
        mocked_internet_connection: bool
) -> None:
    mocked_valid_url.return_value = True
    mocked_internet_connection.return_value = False
    assert can_access_google_page("https://mate.academy") == "Not accessible"
