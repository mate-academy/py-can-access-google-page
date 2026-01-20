from unittest.mock import patch, Mock

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mock_has_internet_connection: Mock,
        mock_valid_google_url: Mock
) -> None:
    url = "https://www.google.com"
    can_access_google_page(url)
    mock_valid_google_url.assert_called_once()
    mock_has_internet_connection.assert_called_once()
