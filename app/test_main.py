from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_where_has_internet_connection_is_false(
        mocked_has_internet_connection: str,
        mocked_valid_google_url: str
) -> None:
    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = True
    assert can_access_google_page("") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_where_valid_google_url_is_false(
        mocked_has_internet_connection: str,
        mocked_valid_google_url: str
) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False
    assert can_access_google_page("") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_where_has_internet_connection_and_valid_google_url_are_false(
        mocked_has_internet_connection: str,
        mocked_valid_google_url: str
) -> None:
    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = False
    assert can_access_google_page("") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_where_has_internet_connection_and_valid_google_url_are_true(
        mocked_has_internet_connection: str,
        mocked_valid_google_url: str
) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True
    assert can_access_google_page("") == "Accessible"
