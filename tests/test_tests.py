import pytest
from unittest.mock import patch
from app import main


@patch('app.main.valid_google_url')
@patch('app.main.has_internet_connection')
def test_cannot_access_if_connection_or_valid_url_is_true(mock_internet, mock_valid_url):
    mock_valid_url.return_value = True
    mock_internet.return_value = False
    assert main.can_access_google_page('https://google.com') == 'Not accessible'

    mock_valid_url.return_value = False
    mock_internet.return_value = True
    assert main.can_access_google_page('https://google.com') == 'Not accessible'


@patch('app.main.valid_google_url')
@patch('app.main.has_internet_connection')
def test_cannot_access_if_only_connection(mock_internet, mock_valid_url):
    mock_valid_url.return_value = False
    mock_internet.return_value = True
    assert main.can_access_google_page('https://google.com') == 'Not accessible'


@patch('app.main.valid_google_url')
@patch('app.main.has_internet_connection')
def test_cannot_access_if_only_valid_url(mock_internet, mock_valid_url):
    mock_valid_url.return_value = True
    mock_internet.return_value = False
    assert main.can_access_google_page('https://google.com') == 'Not accessible'


@patch('app.main.valid_google_url')
@patch('app.main.has_internet_connection')
def test_accessible(mock_internet, mock_valid_url):
    mock_valid_url.return_value = True
    mock_internet.return_value = True
    assert main.can_access_google_page('https://www.google.com') == 'Accessible'


@patch('app.main.valid_google_url')
@patch('app.main.has_internet_connection')
def test_invalid_url(mock_internet, mock_valid_url):
    mock_valid_url.return_value = False
    mock_internet.return_value = True
    assert main.can_access_google_page('https://invalid.url') == 'Not accessible'


@patch('app.main.valid_google_url')
@patch('app.main.has_internet_connection')
def test_no_internet(mock_internet, mock_valid_url):
    mock_valid_url.return_value = True
    mock_internet.return_value = False
    assert main.can_access_google_page('https://www.google.com') == 'Not accessible'


@patch('app.main.valid_google_url')
@patch('app.main.has_internet_connection')
def test_both_invalid(mock_internet, mock_valid_url):
    mock_valid_url.return_value = False
    mock_internet.return_value = False
    assert main.can_access_google_page('https://invalid.url') == 'Not accessible'
