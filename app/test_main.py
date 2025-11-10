from unittest.mock import patch
from app.main import can_access_google_page


@patch('app.main.valid_google_url')
@patch('app.main.has_internet_connection')
def test_can_access_google_page_accessible(mock_valid_google_url, mock_has_internet_connection):
	mock_valid_google_url.return_value = True
	mock_has_internet_connection.return_value = True
	result = can_access_google_page(url='https://www.google.com')
	assert result == "Accessible"

def test_can_access_google_page_not_accessible_first(mock_valid_google_url, mock_has_internet_connection):
	mock_valid_google_url.return_value = True
	mock_has_internet_connection.return_value = False
	result = can_access_google_page(url='https://www.google.com')
	assert result ==" Not accessible"

def test_can_access_google_page_not_accessible_second(mock_valid_google_url, mock_has_internet_connection):
	mock_valid_google_url.return_value = False
	mock_has_internet_connection.return_value = True
	result = can_access_google_page(url='https://www.google.com')
	assert result ==" Not accessible"

def test_can_access_google_page_not_accessible_third(mock_valid_google_url, mock_has_internet_connection):
	mock_valid_google_url.return_value = False
	mock_has_internet_connection.return_value = False
	result = can_access_google_page(url='https://www.google.com')
	assert result ==" Not accessible"