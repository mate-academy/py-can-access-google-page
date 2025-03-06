import pytest
from app.main import can_access_google_page, valid_google_url, has_internet_connection


def test_can_access_google_page_accessible(mocker):
    # Mock both functions to return True
    mocker.patch('app.main.valid_google_url', return_value=True)
    mocker.patch('app.main.has_internet_connection', return_value=True)

    # Test with a valid URL
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


def test_can_access_google_page_not_accessible_invalid_url(mocker):
    # Mock has_internet_connection to return True, but valid_google_url to return False
    mocker.patch('app.main.valid_google_url', return_value=False)
    mocker.patch('app.main.has_internet_connection', return_value=True)

    # Test with an invalid URL
    result = can_access_google_page("https://www.invalidurl.com")
    assert result == "Not accessible"


def test_can_access_google_page_not_accessible_no_internet(mocker):
    # Mock has_internet_connection to return False, but valid_google_url to return True
    mocker.patch('app.main.valid_google_url', return_value=True)
    mocker.patch('app.main.has_internet_connection', return_value=False)

    # Test with a valid URL but no internet connection
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


def test_can_access_google_page_not_accessible_invalid_url_and_no_internet(mocker):
    # Mock both functions to return False
    mocker.patch('app.main.valid_google_url', return_value=False)
    mocker.patch('app.main.has_internet_connection', return_value=False)

    # Test with an invalid URL and no internet connection
    result = can_access_google_page("https://www.invalidurl.com")
    assert result == "Not accessible"