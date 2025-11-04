from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_when_url_is_valid_and_connection_exists(
        mock_internet: MagicMock,
        mock_url: MagicMock
) -> None:
    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_no_internet_but_valid_url(
        mock_internet: MagicMock,
        mock_url: MagicMock
) -> None:
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_valid_internet_but_invalid_url(
        mock_internet: MagicMock,
        mock_url: MagicMock
) -> None:
    result = can_access_google_page("https://invalid-url.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=False)
def test_cannot_access_google_page_when_url_is_invalid_and_no_connection(
        mock_internet: MagicMock,
        mock_url: MagicMock
) -> None:
    result = can_access_google_page("https://invalid-url.com")
    assert result == "Not accessible"
