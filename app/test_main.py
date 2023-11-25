from unittest.mock import MagicMock, patch

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(
    mock_internet_connection: MagicMock,
    mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_internet_connection.return_value = True

    result = can_access_google_page("https://www.google.com")

    assert result == "Accessible"
