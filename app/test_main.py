from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_internet: MagicMock,
                                mock_valid_url: MagicMock) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True

    assert can_access_google_page("https://www.google.com") == "Accessible"
