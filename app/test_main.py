from unittest.mock import MagicMock, patch

from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_accessible_when_url_valid_and_has_connection(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    result = can_access_google_page("https://www.google.com")

    assert result == "Accessible"
    mock_valid_google_url.assert_called_once_with(
        "https://www.google.com"
    )
    mock_has_internet_connection.assert_called_once_with()


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_not_accessible_when_url_invalid(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    result = can_access_google_page("https://example.com")

    assert result == "Not accessible"
    mock_valid_google_url.assert_called_once_with(
        "https://example.com"
    )
    mock_has_internet_connection.assert_called_once_with()


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_not_accessible_when_no_connection(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"
    mock_has_internet_connection.assert_called_once_with()
    mock_valid_google_url.assert_not_called()


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_not_accessible_when_url_invalid_and_no_connection(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False

    result = can_access_google_page("https://example.com")

    assert result == "Not accessible"
    mock_has_internet_connection.assert_called_once_with()
    mock_valid_google_url.assert_not_called()
