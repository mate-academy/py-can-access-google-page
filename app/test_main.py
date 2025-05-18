from unittest.mock import patch, Mock
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_accessible_when_both_true(
        mock_internet: Mock,
        mock_url: Mock
) -> None:
    mock_internet.return_value = True
    mock_url.return_value = True

    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_no_internet(
        mock_internet: Mock,
        mock_url: Mock
) -> None:
    mock_internet.return_value = False
    mock_url.return_value = True

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_url_invalid(
        mock_internet: Mock,
        mock_url: Mock
) -> None:
    mock_internet.return_value = True
    mock_url.return_value = False

    result = can_access_google_page("https://invalid-url.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_both_false(
        mock_internet: Mock,
        mock_url: Mock
) -> None:
    mock_internet.return_value = False
    mock_url.return_value = False

    result = can_access_google_page("https://invalid-url.com")
    assert result == "Not accessible"
