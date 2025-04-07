from unittest.mock import MagicMock, patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_accessible_when_valid_and_connected(
    mock_internet: MagicMock, mock_valid_url: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_only_url_is_valid(
    mock_internet: MagicMock, mock_valid_url: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_only_internet(
    mock_internet: MagicMock, mock_valid_url: MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_both_false(
    mock_internet: MagicMock, mock_valid_url: MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
