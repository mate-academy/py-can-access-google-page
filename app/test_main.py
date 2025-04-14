from app.main import can_access_google_page
from unittest import mock

@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def tests_can_access(mock_valid_url, mock_internet):
    mock_internet.return_value = True
    mock_valid_url.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"

@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mock_valid_url, mock_internet):
    mock_internet.return_value = True
    mock_valid_url.return_value = True

    result = can_access_google_page("https://google.com")
    assert result == "Accessible"

@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_no_internet(mock_valid_url, mock_internet):
    mock_internet.return_value = False
    mock_valid_url.return_value = True

    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"

@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_invalid_url(mock_valid_url, mock_internet):
    mock_internet.return_value = True
    mock_valid_url.return_value = False

    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"