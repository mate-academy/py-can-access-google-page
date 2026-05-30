from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_accessible_when_valid_url_and_internet(
    mock_internet: MagicMock, mock_url: MagicMock
) -> None:
    mock_internet.return_value = True
    mock_url.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_valid_no_internet(
    mock_internet: MagicMock, mock_url: MagicMock
) -> None:
    mock_internet.return_value = False
    mock_url.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_valid_url(
    mock_internet: MagicMock, mock_url: MagicMock
) -> None:
    mock_internet.return_value = True
    mock_url.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_no_internet_and_invalid_url(
        mock_internet: MagicMock,
        mock_url: MagicMock
) -> None:
    mock_internet.return_value = False
    mock_url.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_has_internet_connection_is_called(
        mock_internet: MagicMock,
        mock_url: MagicMock
) -> None:
    mock_internet.return_value = True
    mock_url.return_value = True
    can_access_google_page("https://google.com")
    mock_internet.assert_called_once_with()


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_valid_google_url_is_called_with_correct_url(
        mock_internet: MagicMock,
        mock_url: MagicMock
) -> None:
    mock_internet.return_value = True
    mock_url.return_value = True
    can_access_google_page("https://google.com")
    mock_url.assert_called_once_with("https://google.com")
