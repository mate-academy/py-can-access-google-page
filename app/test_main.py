from unittest.mock import Mock
from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_internet: Mock, mock_url: Mock) -> None:
    mock_url.return_value = True
    mock_internet.return_value = True
    result = can_access_google_page("https://google.com")
    assert result == "Accessible"
