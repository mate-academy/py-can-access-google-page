from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
def test_check_valid_url(
        mocked_valid_google_url: mock.MagicMock
) -> None:
    can_access_google_page("https://www.youtube.com/")
    mocked_valid_google_url.assert_called_once_with("https://www.youtube.com/")


@mock.patch("app.main.has_internet_connection")
def test_check_internet_connection(
        mocked_has_internet_connection: mock.MagicMock
) -> None:
    can_access_google_page("https://www.youtube.com/")
    mocked_has_internet_connection.assert_called_once()
