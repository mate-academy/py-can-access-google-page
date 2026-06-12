from unittest.mock import patch, MagicMock
import app.main as main


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_is_valid_google_url_and_has_internet(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    result = main.can_access_google_page("https://www.google.com")

    assert result == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_is_valid_google_url_and_not_internet(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    result = main.can_access_google_page("https://www.google.com")

    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_is_invalid_google_url_and_has_internet(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    result = main.can_access_google_page("https://www.google.com")

    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_is_invalid_google_url_and_no_internet(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False

    result = main.can_access_google_page("https://www.google.com")

    assert result == "Not accessible"
