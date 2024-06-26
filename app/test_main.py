from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_with_no_internet(
    mocked_url: mock.Mock,
    mocked_internet_connection: mock.Mock
) -> None:
    mocked_url.return_value = True
    mocked_internet_connection.return_value = False

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"

    mocked_url.assert_called()
    mocked_internet_connection.assert_called()


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_with_invalid_url(
    mocked_url: mock.Mock,
    mocked_internet_connection: mock.Mock
) -> None:
    mocked_url.return_value = False
    mocked_internet_connection.return_value = True

    result = can_access_google_page("https://invalid-url.com")
    assert result == "Not accessible"

    mocked_url.assert_called()
    mocked_internet_connection.assert_called()
