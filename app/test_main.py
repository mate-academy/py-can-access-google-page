from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_internal_functions_are_called(
        mocked_has_internet_connection: mock.Mock,
        mocked_has_valid_google_url: mock.Mock
) -> None:
    can_access_google_page("")
    mocked_has_internet_connection.assert_called_once()
    mocked_has_valid_google_url.assert_called_once()


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(
        mocked_has_internet_connection: mock.Mock,
        mocked_has_valid_google_url: mock.Mock
) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_has_valid_google_url.return_value = True
    assert can_access_google_page("") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_connection_missing(
        mocked_has_internet_connection: mock.Mock,
        mocked_has_valid_google_url: mock.Mock
) -> None:
    mocked_has_internet_connection.return_value = False
    mocked_has_valid_google_url.return_value = True
    assert can_access_google_page("") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_invalid_url_and_connection_missing(
        mocked_has_internet_connection: mock.Mock,
        mocked_has_valid_google_url: mock.Mock
) -> None:
    mocked_has_internet_connection.return_value = False
    mocked_has_valid_google_url.return_value = False
    assert can_access_google_page("") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_invalid_url_and_connection_exists(
        mocked_has_internet_connection: mock.Mock,
        mocked_has_valid_google_url: mock.Mock
) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_has_valid_google_url.return_value = False
    assert can_access_google_page("") == "Not accessible"
