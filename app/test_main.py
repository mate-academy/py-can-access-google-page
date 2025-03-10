import pytest
from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page_accessible():
    with patch('app.main.valid_google_url', return_value=True):
        with patch('app.main.has_internet_connection', return_value=True):
            assert can_access_google_page('http://www.google.com') == 'Accessible'

def test_can_access_google_page_not_valid_url():
    with patch('app.main.valid_google_url', return_value=False):
        with patch('app.main.has_internet_connection', return_value=True):
            assert can_access_google_page('http://www.invalidurl.com') == 'Not accessible'

def test_can_access_google_page_no_internet():
    with patch('app.main.valid_google_url', return_value=True):
        with patch('app.main.has_internet_connection', return_value=False):
            assert can_access_google_page('http://www.google.com') == 'Not accessible'
