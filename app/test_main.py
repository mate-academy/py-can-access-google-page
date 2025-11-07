from unittest import mock

from app.main import can_access_google_page


@mock.patch("requests.get")
def test_valid_google_url_called(mock_get: mock.MagicMock) -> None:
    can_access_google_page("https://google.com")
    mock_get.assert_called_with("https://google.com")


@mock.patch("app.main.datetime")
def test_has_internet_connection_called(mock_datetime: mock.MagicMock) -> None:
    can_access_google_page("https://google.com")
    mock_datetime.datetime.now.assert_called()
