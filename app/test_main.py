from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(mock_internet, mock_valid_url):
    mock_valid_url.return_value = True
    mock_internet.return_value = True
    assert can_access_google_page("test.pl") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cant_access_google_page_when_no_internet(mock_internet, mock_valid_url):
    mock_valid_url.return_value = True
    mock_internet.return_value = False
    assert can_access_google_page("test.pl") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cant_access_google_page_when_bad_link(mock_internet, mock_valid_url):
    mock_valid_url.return_value = False
    mock_internet.return_value = True
    assert can_access_google_page("test.pl") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cant_access_google_page_when_bad_link_and_no_internet(mock_internet, mock_valid_url):
    mock_valid_url.return_value = False
    mock_internet.return_value = False
    assert can_access_google_page("test.pl") == "Not accessible"
