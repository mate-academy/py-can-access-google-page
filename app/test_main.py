from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_with_url_and_internet(
        mock_has_internet_connection: mock.MagicMock,
        mock_valid_google_url: mock.MagicMock) -> None:
    can_access_google_page("www.google.com")
    mock_has_internet_connection.assert_called_once()
    mock_valid_google_url.assert_called_once_with("www.google.com")
