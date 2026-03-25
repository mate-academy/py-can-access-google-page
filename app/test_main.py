from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_returns_accessible_with_valid_url_and_connection(
    mock_valid_url: MagicMock,
    mock_internet: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_returns_not_accessible_with_invalid_url(
    mock_valid_url: MagicMock,
    mock_internet: MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_return_not_accessible_when_no_internet(
    mock_valid_url: MagicMock,
    mock_internet: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"
