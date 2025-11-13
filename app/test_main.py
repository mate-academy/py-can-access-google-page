from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True

    result = can_access_google_page("https://google.com")

    assert result == "Accessible"
    mock_has_internet_connection.assert_called_once()
    mock_valid_google_url.assert_called_once_with("https://google.com")


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_with_no_internet_connection(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_has_internet_connection.return_value = False
    result = can_access_google_page("https://google.com")

    assert result == "Not accessible"
    mock_has_internet_connection.assert_called_once()
    mock_valid_google_url.assert_not_called()


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_with_invalid_url(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False

    result = can_access_google_page("https://not-google.com")

    assert result == "Not accessible"
    mock_has_internet_connection.assert_called_once()
    mock_valid_google_url.assert_called_once_with("https://not-google.com")
