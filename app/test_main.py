from unittest.mock import Mock

from app.main import can_access_google_page

from unittest import mock


@mock.patch("main.valid_google_url", return_value=True)
@mock.patch("main.has_internet_connection", return_value=True)
def test_can_access_google_page_success(mock_internet: Mock,
                                        mock_url: Mock) -> None:
    result = can_access_google_page("https://google.com")
    assert result == "Accessible"
    mock_internet.assert_called_once()
    mock_url.assert_called_once_with("https://google.com")
