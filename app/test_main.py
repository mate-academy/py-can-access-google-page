from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_accessible_case(mock_internet, mock_valid_url):
    mock_valid_url.return_value = True
    mock_internet.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_invalid_url(mock_internet, mock_valid_url):
    mock_valid_url.return_value = False
    mock_internet.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_no_internet(mock_internet, mock_valid_url):
    mock_valid_url.return_value = True
    mock_internet.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_both_invalid(mock_internet, mock_valid_url):
    mock_valid_url.return_value = False
    mock_internet.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"