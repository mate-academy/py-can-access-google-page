from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page(
        mock_has_internet: MagicMock, mock_valid_url: MagicMock) -> None:
    url_test = "https://www.google.com"
    result = can_access_google_page(url_test)
    assert result == "Accessible"

    mock_has_internet.assert_called_once()
    mock_valid_url.assert_called_once_with(url_test)
