from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
def test_valid_google_url(mocked_url: mock.MagicMock) -> None:
    can_access_google_page("https://google.com")
    mocked_url.assert_called_once_with("https://google.com")


@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection(mocked_internet: mock.MagicMock) -> None:
    can_access_google_page("https://google.com")
    mocked_internet.assert_called_once()
