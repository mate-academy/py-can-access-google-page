from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_with_valid_url(
        mocked_url: mock.MagicMock
) -> None:
    can_access_google_page("https://www.google.com/")
    mocked_url.assert_called_once_with("https://www.google.com/")


@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_with_internet_connection(
        mocked_internet: mock.MagicMock
) -> None:
    can_access_google_page("https://www.google.com/")
    mocked_internet.assert_called_once()
