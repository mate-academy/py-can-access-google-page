from unittest.mock import MagicMock, patch

from app.main import can_access_google_page


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page(
    mocked_valid_google_url: MagicMock,
    mocked_has_internet_connection: MagicMock,
) -> None:
    url = "https://www.google.com"
    result = can_access_google_page(url)
    mocked_has_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_once_with(url)
    assert result == "Accessible"
