from unittest.mock import MagicMock, patch
from app.main import can_access_google_page

url = "https://www.notavalidurl.com"


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page_access_granted(
    mock_valid_url: MagicMock, mock_internet: MagicMock
) -> None:
    assert can_access_google_page(url) == "Accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page_no_internet(mock_valid_url: MagicMock,
                                            mock_internet: MagicMock) -> None:
    assert can_access_google_page(url) == "Not accessible"


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=False)
def test_can_access_google_page_invalid_url(mock_valid_url: MagicMock,
                                            mock_internet: MagicMock) -> None:
    assert can_access_google_page(url) == "Not accessible"
