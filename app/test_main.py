from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_has_internet_connection: mock,
                                mock_valid_google_url: mock) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True
    can_access_google_page("https://www.google.com")
    mock_has_internet_connection.assert_called_once()
    mock_valid_google_url.assert_called_once()
