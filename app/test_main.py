from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_wih_connection_and_url(
        mocked_has_connection: mock.MagicMock,
        mocked_valid_url: mock.MagicMock) -> None:
    mocked_valid_url.return_value = True
    mocked_has_connection.return_value = True
    assert can_access_google_page("https://data.rocks") == "Accessible"

    mocked_valid_url.assert_called()
    mocked_has_connection.assert_called()


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_wih_no_connection(
        mocked_has_connection: mock.MagicMock,
        mocked_valid_url: mock.MagicMock) -> None:
    mocked_valid_url.return_value = True
    mocked_has_connection.return_value = False
    assert can_access_google_page("https://data.rocks") == "Not accessible"

    mocked_valid_url.assert_called()
    mocked_has_connection.assert_called()


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_wih_not_valid_url(
        mocked_has_connection: mock.MagicMock,
        mocked_valid_url: mock.MagicMock) -> None:
    mocked_valid_url.return_value = False
    mocked_has_connection.return_value = True

    assert can_access_google_page("https://data.rocks") == "Not accessible"
