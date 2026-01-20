from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_accessible_case(
    mock_internet: MagicMock,
    mock_valid_url: MagicMock,
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_invalid_url(
    mock_internet: MagicMock,
    mock_valid_url: MagicMock,
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_no_internet(
    mock_internet: MagicMock,
    mock_valid_url: MagicMock,
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_both_invalid(
    mock_internet: MagicMock,
    mock_valid_url: MagicMock,
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
