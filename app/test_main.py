from unittest.mock import MagicMock, patch
from app.main import can_access_google_page


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page_accessible(
        mock_valid_url: MagicMock,
        mock_internet: MagicMock
) -> None:
    result = can_access_google_page("https://google.com")

    mock_internet.assert_called_once()
    mock_valid_url.assert_called_once_with("https://google.com")

    assert result == "Accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page_not_accessible_without_connection(
        mock_valid_url: MagicMock,
        mock_internet: MagicMock
) -> None:
    result = can_access_google_page("https://www.google.com")

    mock_internet.assert_called_once()
    mock_valid_url.assert_not_called()

    assert result == "Not accessible"


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=False)
def test_can_access_google_page_not_accessible_with_invalid_url(
        mock_valid_url: MagicMock,
        mock_internet: MagicMock
) -> None:
    result = can_access_google_page("https://www.google.com")

    mock_internet.assert_called_once()
    mock_valid_url.assert_called_once_with("https://www.google.com")

    assert result == "Not accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=False)
def test_can_access_google_page_not_accessible_no_internet_invalid_url(
        mock_valid_url: MagicMock,
        mock_internet: MagicMock
) -> None:
    result = can_access_google_page("https://invalid.com")

    mock_internet.assert_called_once()
    mock_valid_url.assert_not_called()

    assert result == "Not accessible"
