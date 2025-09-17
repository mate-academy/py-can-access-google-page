from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_has_internet: MagicMock, mock_valid_url: MagicMock) -> None:
    mock_has_internet.return_value = True
    mock_valid_url.return_value = True

    result = can_access_google_page("https://www.google.com/")
    assert result == "Accessible"

    mock_has_internet.assert_called_once()
    mock_valid_url.assert_called_once_with("https://www.google.com/")
