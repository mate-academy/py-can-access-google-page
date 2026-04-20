from unittest.mock import MagicMock, patch

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_returns_accessible_when_url_is_valid_and_connection_exists(
    mock_has_internet_connection: MagicMock,
    mock_valid_google_url: MagicMock,
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True

    assert can_access_google_page("https://www.google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_returns_not_accessible_when_url_is_not_valid(
    mock_has_internet_connection: MagicMock,
    mock_valid_google_url: MagicMock,
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_returns_not_accessible_when_connection_does_not_exist(
    mock_has_internet_connection: MagicMock,
    mock_valid_google_url: MagicMock,
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True

    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_returns_not_accessible_when_url_is_not_valid_and_connection_is_absent(
    mock_has_internet_connection: MagicMock,
    mock_valid_google_url: MagicMock,
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"
