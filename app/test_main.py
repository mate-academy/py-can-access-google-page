from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_called_functions(
        mocked_has_internet_connection: mock.Mock,
        mocked_has_valid_google_url: mock.Mock
) -> None:
    can_access_google_page("")
    mocked_has_internet_connection.assert_called_once()
    mocked_has_valid_google_url.assert_called_once()


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_values(
        mocked_has_internet_connection: mock.Mock,
        mocked_has_valid_google_url: mock.Mock
) -> None:
    can_access_google_page("")
    mocked_has_internet_connection.return_value = True
    mocked_has_valid_google_url.return_value = True
    assert can_access_google_page("") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_first_invalid_values(
        mocked_has_internet_connection: mock.Mock,
        mocked_has_valid_google_url: mock.Mock
) -> None:
    can_access_google_page("")
    mocked_has_internet_connection.return_value = False
    mocked_has_valid_google_url.return_value = True
    assert can_access_google_page("") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_second_invalid_values(
        mocked_has_internet_connection: mock.Mock,
        mocked_has_valid_google_url: mock.Mock
) -> None:
    can_access_google_page("")
    mocked_has_internet_connection.return_value = True
    mocked_has_valid_google_url.return_value = False
    assert can_access_google_page("") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_both_invalid_values(
        mocked_has_internet_connection: mock.Mock,
        mocked_has_valid_google_url: mock.Mock
) -> None:
    can_access_google_page("")
    mocked_has_internet_connection.return_value = False
    mocked_has_valid_google_url.return_value = False
    assert can_access_google_page("") == "Not accessible"
