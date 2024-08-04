from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(
        mock_has_internet_connection: str,
        mock_valid_google_url: str
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_not_accessible_no_internet(
        mock_has_internet_connection: str,
        mock_valid_google_url: str
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_not_accessible_invalid_url(
        mock_has_internet_connection: str,
        mock_valid_google_url: str
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_not_accessible_due_to_both(
        mock_has_internet_connection: str,
        mock_valid_google_url: str
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
