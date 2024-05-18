from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_internet, mock_url):
    mock_internet.return_value = True
    mock_url.return_value = False
    can_access_google_page("https://www.notrealurl.com")
    mock_internet.assert_called_once_with()
    mock_url.assert_called_once_with("https://www.notrealurl.com")
