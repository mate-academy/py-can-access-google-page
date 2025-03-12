# write your code here
from app.main import can_access_google_page
from unittest.mock import patch


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_to_google_page(mock_has_internet, mock_valid_google_url) -> None:
    mock_has_internet.return_value = True
    mock_valid_google_url.return_value = True
    result = can_access_google_page("http://www.google.com")
    assert result == "Accessible"



@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_to_google_page_no_internet(mock_has_internet, mock_valid_google_url) -> None:
    mock_has_internet.return_value = False
    mock_valid_google_url.return_value = True
    result = can_access_google_page("http://www.google.com")
    assert result == "Not Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_to_google_page_invalid_url(mock_has_internet, mock_valid_google_url) -> None:
    mock_has_internet.return_value = True
    mock_valid_google_url.return_value = False
    result = can_access_google_page("http://www.google.com")
    assert result == "Not Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_to_google_page_invalid_url_no_connection(mock_has_internet, mock_valid_google_url) -> None:
    mock_has_internet.return_value = False
    mock_valid_google_url.return_value = False
    result = can_access_google_page("http://www.google.com")
    assert result == "Not Accessible"
