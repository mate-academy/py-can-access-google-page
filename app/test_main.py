from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_url_true_connection_true(mock_url,
                                                         mock_connection):
    mock_url.return_value = True
    mock_connection.return_value = True
    result = can_access_google_page("https://www.google.com.ua/")
    assert result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_url_true_connection_false(mock_url,
                                                          mock_connection):
    mock_url.return_value = True
    mock_connection.return_value = False
    result = can_access_google_page("https://www.google.com.ua/")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_url_false_connection_true(mock_url,
                                                          mock_connection):
    mock_url.return_value = False
    mock_connection.return_value = True
    result = can_access_google_page("https://www.google.com.ua/")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_url_false_connection_false(mock_url,
                                                           mock_connection):
    mock_url.return_value = False
    mock_connection.return_value = False
    result = can_access_google_page("https://www.google.com.ua/")
    assert result == "Not accessible"
