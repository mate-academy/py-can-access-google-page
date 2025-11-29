from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet: MagicMock, mock_valid_url: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"

    mock_valid_url.return_value = False
    mock_has_internet.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"

    mock_valid_url.return_value = True
    mock_has_internet.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"

    mock_valid_url.return_value = False
    mock_has_internet.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
