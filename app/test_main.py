from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_accessible_when_connection_and_valid_url(
    mock_has_connection: patch,
    mock_valid_url: patch
) -> None:
    mock_has_connection.return_value = True
    mock_valid_url.return_value = True

    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_no_connection_but_valid_url(
    mock_has_connection: patch,
    mock_valid_url: patch
) -> None:
    mock_has_connection.return_value = False
    mock_valid_url.return_value = True

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_connection_but_invalid_url(
    mock_has_connection: patch,
    mock_valid_url: patch
) -> None:
    mock_has_connection.return_value = True
    mock_valid_url.return_value = False

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_no_connection_and_invalid_url(
    mock_has_connection: patch,
    mock_valid_url: patch
) -> None:
    mock_has_connection.return_value = False
    mock_valid_url.return_value = False

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
