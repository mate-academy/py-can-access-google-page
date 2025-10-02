from unittest.mock import MagicMock, patch
from .main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_access_google_page_correctly(
    mock_url: MagicMock,
    mock_connection: MagicMock
) -> None:
    mock_url.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page("google.com") == "Accessible"
    mock_connection.assert_called_once()
    mock_url.assert_called_once_with("google.com")
