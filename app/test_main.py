from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(mock_has_internet_connection,
                                           mock_valid_google_url):
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True
    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_not_accessible_no_connection\
                (mock_has_internet_connection, mock_valid_google_url):
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_not_accessible_invalid_url\
                (mock_has_internet_connection, mock_valid_google_url):
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False
    result = can_access_google_page("https://example.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_not_accessible_invalid_url_no_connection\
                (mock_has_internet_connection, mock_valid_google_url):
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = False
    result = can_access_google_page("https://example.com")
    assert result == "Not accessible"
