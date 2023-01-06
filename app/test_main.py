from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_when_has_internet_and_url_is_valid(
        mocked_has_internet_connection: callable,
        mocked_valid_google_url: callable
) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True
    assert can_access_google_page("example_of_url") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_when_has_not_internet_and_url_is_valid(
        mocked_has_internet_connection: callable,
        mocked_valid_google_url: callable
) -> None:
    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = True
    assert can_access_google_page("example_of_url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_when_has_internet_and_url_is_not_valid(
        mocked_has_internet_connection: callable,
        mocked_valid_google_url: callable
) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False
    assert can_access_google_page("example_of_url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_when_has_not_internet_and_url_is_not_valid(
        mocked_has_internet_connection: callable,
        mocked_valid_google_url: callable
) -> None:
    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = False
    assert can_access_google_page("example_of_url") == "Not accessible"
