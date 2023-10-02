from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_all_true(
        mocked_connection,
        mocked_url
) -> None:
    mocked_connection.return_value = True
    mocked_url.return_value = True

    result = can_access_google_page("https://www.google.com.ua/")
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_connection_false(
        mocked_connection,
        mocked_url
) -> None:
    mocked_connection.return_value = False
    mocked_url.return_value = True

    result = can_access_google_page("https://www.google.com.ua/")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_url_false(
        mocked_connection,
        mocked_url
) -> None:
    mocked_connection.return_value = True
    mocked_url.return_value = False

    result = can_access_google_page("https://www.google.com.ua/")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_all_false(
        mocked_connection,
        mocked_url
) -> None:
    mocked_connection.return_value = False
    mocked_url.return_value = False

    result = can_access_google_page("https://www.google.com.ua/")
    assert result == "Not accessible"
