from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(
        mock_internet: bool, mock_valid_url: bool
) -> None:
    mock_internet.return_value = True
    mock_valid_url.return_value = True
    assert can_access_google_page(
        "https://www.google.com"
    ) == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_not_accessible_no_internet(
        mock_internet: bool, mock_valid_url: bool
) -> None:
    mock_internet.return_value = False
    mock_valid_url.return_value = True
    assert can_access_google_page(
        "https://www.google.com"
    ) == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_not_accessible_invalid_url(
        mock_internet: bool, mock_valid_url: bool
) -> None:
    mock_internet.return_value = True
    mock_valid_url.return_value = False
    assert can_access_google_page(
        "https://invalid-url.com"
    ) == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_not_accessible_both_false(
        mock_internet: bool, mock_valid_url: bool
) -> None:
    mock_internet.return_value = False
    mock_valid_url.return_value = False
    assert can_access_google_page(
        "https://invalid-url.com"
    ) == "Not accessible"
