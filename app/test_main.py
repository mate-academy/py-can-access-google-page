from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mock_valid_url: mock.MagicMock,
                                mock_internet: mock.MagicMock) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True
    result = can_access_google_page("https://google.com")
    assert result == "Accessible"
    mock_internet.assert_called_once()
    mock_valid_url.assert_called_once_with("https://google.com")
