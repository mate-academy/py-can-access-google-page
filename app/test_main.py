from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("main.has_internet_connection")
@patch("main.valid_google_url")
def test_can_access_google_page(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True
    assert can_access_google_page("http://www.google.com") == "Accessible"

    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True
    assert can_access_google_page("http://www.google.com") == "Not accessible"

    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False
    assert can_access_google_page("http://www.google.com") == "Not accessible"

    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = False
    assert can_access_google_page("http://www.google.com") == "Not accessible"