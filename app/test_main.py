from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_accessible_when_url_valid_and_internet_connected(
        mock_valid_url,
        mock_has_internet
):
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True

    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_not_accessible_when_internet_disconnected(
        mock_valid_url,
        mock_has_internet
):
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False

    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_not_accessible_when_url_is_invalid(
        mock_valid_url,
        mock_has_internet
):
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True

    result = can_access_google_page("https://invalid-url.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_not_accessible_when_both_conditions_fail(
        mock_valid_url,
        mock_has_internet
):
    """Should return 'Not accessible' if both criteria fail"""
    mock_valid_url.return_value = False
    mock_has_internet.return_value = False

    result = can_access_google_page("https://invalid-url.com")
    assert result == "Not accessible"


