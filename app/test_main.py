from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_success(
        mock_valid: MagicMock,
        mock_internet: MagicMock
) -> None:

    mock_valid.return_value = True
    mock_internet.return_value = True

    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_no_time(
        mock_valid: MagicMock,
        mock_internet: MagicMock
) -> None:
    mock_valid.return_value = False
    mock_internet.return_value = True

    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_no_internet(
        mock_valid: MagicMock,
        mock_internet: MagicMock
) -> None:
    mock_valid.return_value = True
    mock_internet.return_value = False

    result = can_access_google_page("https://bad-url.com")
    assert result == "Not accessible"
