import pytest
from unittest import mock
from app import main

def mock_valid_google_url(url):
    if url == "https://www.google.com/":
        return True
    else:
        return False

def test_valid_google_url1():
    with mock.patch('app.main.valid_google_url', side_effect=mock_valid_google_url):
        assert main.can_access_google_page("https://www.example.com/") == "Not accessible"

def test_can_access_google_page7():
    with mock.patch('app.main.valid_google_url', side_effect=mock_valid_google_url), \
            mock.patch('app.main.has_internet_connection', return_value=True):
        access_google = main.can_access_google_page("https://www.google.com/")
        assert access_google == "Accessible"

def mock_has_internet_connection():
    return True  # Змінено значення повернення на True

def test_cannot_access_if_only_valid_url11():
    with mock.patch('app.main.valid_google_url', side_effect=mock_valid_google_url), \
            mock.patch('app.main.has_internet_connection', side_effect=mock_has_internet_connection):
        result1 = main.can_access_google_page("https://www.google.com/")
        assert result1 == 'Accessible'

def test_cannot_access_if_only_valid_url12():
    with mock.patch('app.main.valid_google_url', side_effect=mock_valid_google_url), \
            mock.patch('app.main.has_internet_connection', return_value=False):
        result2 = main.can_access_google_page("https://www.google.com/aa")
        assert result2 == 'Not accessible'

def test_cannot_access_if_only_valid_url(monkeypatch):
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    result1 = main.can_access_google_page("https://www.google.com/")
    result2 = main.can_access_google_page("https://www.example.com/")
    result3 = main.can_access_google_page("https://www.anotherurl.com/")
    assert result1 == "Not accessible"
    assert result2 == "Not accessible"
    assert result3 == "Not accessible"
