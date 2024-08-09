from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_connect_if_has_correct_url_and_correct_time(
        mocked_has_internet_connection: bool,
        mocked_google_url: bool
) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_google_url.return_value = True
    assert can_access_google_page("http://www.google.com") == "Accessible"


@mock.patch("main.valid_google_url")
@mock.patch("main.has_internet_connection")
def test_not_connect_if_has_not_correct_url_and_has_correct_time(
        mocked_has_internet_connection: bool,
        mocked_google_url: bool
) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_google_url.return_value = False
    assert can_access_google_page("http://www.google.com") == "Not accessible"


@mock.patch("main.valid_google_url")
@mock.patch("main.has_internet_connection")
def test_not_connect_if_has_not_correct_url_and_not_correct_time(
        mocked_has_internet_connection: bool,
        mocked_google_url: bool
) -> None:
    mocked_has_internet_connection.return_value = False
    mocked_google_url.return_value = False
    assert can_access_google_page("http://www.google.com") == "Not accessible"


@mock.patch("main.valid_google_url")
@mock.patch("main.has_internet_connection")
def test_not_connect_if_has_correct_url_and_not_correct_time(
        mocked_has_internet_connection: bool,
        mocked_google_url: bool
) -> None:
    mocked_has_internet_connection.return_value = False
    mocked_google_url.return_value = True
    assert can_access_google_page("http://www.google.com") == "Not accessible"
