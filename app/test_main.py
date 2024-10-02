from unittest.mock import patch
from app.main import can_access_google_page


# Test when the URL is valid and internet connection is available
@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_accessible(
    mock_internet: bool, mock_url: bool
) -> None:
    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == "Accessible"


# Test when the URL is not valid but internet connection is available
@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_not_accessible_due_to_url(
    mock_internet: bool, mock_url: bool
) -> None:
    url = "https://www.invalid-url.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"


# Test when the internet connection is not available but the URL is valid
@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_not_accessible_due_to_internet(
    mock_internet: bool, mock_url: bool
) -> None:
    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"


# Test when neither the internet nor the URL are valid
@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_not_accessible(
    mock_internet: bool, mock_url: bool
) -> None:
    url = "https://www.invalid-url.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"
