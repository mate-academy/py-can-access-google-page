from unittest.mock import patch
from .main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(
        mock_internet: bool,
        mock_valid_url: bool
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True

    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_invalid_url(
        mock_internet: bool,
        mock_valid_url: bool
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = True

    result = can_access_google_page("https://notgoogle.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_no_internet(
        mock_internet: bool,
        mock_valid_url: bool
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = False

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
