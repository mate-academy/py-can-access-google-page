from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_both_value_is_true(
        mocked_valid_google_url: any,
        mocked_has_internet_connection: any
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True

    assert can_access_google_page("http://www.google.com") == "Accessible"

    mocked_has_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_once_with("http://www.google.com")


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_google_url_is_false(
        mocked_valid_google_url: any,
        mocked_has_internet_connection: any
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True

    assert can_access_google_page("http://www.google.com") == "Not accessible"

    mocked_has_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_once_with("http://www.google.com")


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_has_internet_connection_is_false(
        mocked_valid_google_url: any,
        mocked_has_internet_connection: any
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False

    assert can_access_google_page("http://www.google.com") == "Not accessible"

    mocked_has_internet_connection.assert_called_once()


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_both_value_is_false(
        mocked_valid_google_url: any,
        mocked_has_internet_connection: any
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False

    assert can_access_google_page("http://www.google.com") == "Not accessible"

    mocked_has_internet_connection.assert_called_once()
