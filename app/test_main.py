from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_url: MagicMock,
        mock_internet: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"
    mock_valid_url.return_value = False
    mock_internet.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"
    mock_valid_url.return_value = True
    mock_internet.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"
