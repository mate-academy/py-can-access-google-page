from unittest import mock

from app.main import can_access_google_page, valid_google_url, has_internet_connection

@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_internet_connection, mocked_valid_google_url) -> None:
    mocked_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True
    url = "https://www.google.com/"
    assert can_access_google_page(url) == "Accessible"
    mocked_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_once_with(url)

@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cannot_access_if_only_connection(mocked_internet_connection, mocked_valid_google_url) -> None:
    mocked_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False
    url = "invalid_url"
    assert can_access_google_page(url) == "Not accessible"
    mocked_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_once_with(url)


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cannot_access_if_only_valid_url(mocked_internet_connection, mocked_valid_google_url) -> None:
    mocked_internet_connection.return_value = False
    mocked_valid_google_url.return_value = True
    url = "https://www.google.com/"
    assert can_access_google_page(url) == "Not accessible"
    mocked_internet_connection.assert_called_once()

