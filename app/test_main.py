from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(mock_valid_url: MagicMock,
                                mock_internet: MagicMock) -> None:
    mock_internet.return_value = True
    mock_valid_url.return_value = True

    assert can_access_google_page("https://www.google.com") == "Accessible"
