from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch('app.main.valid_google_url', return_value=True)
@patch('app.main.has_internet_connection', return_value=True)
def test_can_access_google_page_accessible(
        mock_valid_url: MagicMock,
        mock_internet_connection: MagicMock
) -> None:
    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == "Accessible"


@patch('app.main.valid_google_url', return_value=True)
@patch('app.main.has_internet_connection', return_value=False)
def test_can_access_google_page_no_internet(
        mock_valid_url: MagicMock,
        mock_internet_connection: MagicMock
) -> None:
    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"


@patch('app.main.valid_google_url', return_value=False)
@patch('app.main.has_internet_connection', return_value=True)
def test_can_access_google_page_invalid_url(
        mock_valid_url: MagicMock,
        mock_internet_connection: MagicMock
) -> None:
    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"


@patch('app.main.valid_google_url', return_value=False)
@patch('app.main.has_internet_connection', return_value=False)
def test_can_access_google_page_invalid_url_and_no_internet_connection(
        mock_valid_url: MagicMock,
        mock_internet_connection: MagicMock
) -> None:
    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"
