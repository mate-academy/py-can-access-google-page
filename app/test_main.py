from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_accessible(
    mock_valid_url: patch, mock_internet_connection: patch
) -> None:
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_not_accessible_no_internet(
    mock_valid_url: patch, mock_internet_connection: patch
) -> None:
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_not_accessible_invalid_url(
    mock_valid_url: patch, mock_internet_connection: patch
) -> None:
    result = can_access_google_page("https://invalid.url")
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_not_accessible_both_invalid(
    mock_valid_url: patch, mock_internet_connection: patch
) -> None:
    result = can_access_google_page("https://invalid.url")
    assert result == "Not accessible"
