from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


@patch('app.main.valid_google_url')
@patch('app.main.has_internet_connection')
def test_valid_url_and_connection_exists(mock_valid_url: MagicMock, mock_has_internet: MagicMock) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True

    assert can_access_google_page("https://www.google.com/") == "Accessible"


@patch('app.main.valid_google_url')
@patch('app.main.has_internet_connection')
def test_invalid_url_and_connection_exists(mock_valid_url: MagicMock, mock_has_internet: MagicMock) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True

    assert can_access_google_page("https://www.google.com/") == "Not accessible"


@patch('app.main.valid_google_url')
@patch('app.main.has_internet_connection')
def test_valid_url_and_no_connection_exists(mock_valid_url: MagicMock, mock_has_internet: MagicMock) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False

    assert can_access_google_page("https://www.google.com/") == "Not accessible"


@patch('app.main.valid_google_url')
@patch('app.main.has_internet_connection')
def test_invalid_url_and_no_connection_exists(mock_valid_url: MagicMock, mock_has_internet: MagicMock) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = False

    assert can_access_google_page("https://www.google.com/") == "Not accessible"
