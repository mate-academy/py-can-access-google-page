from unittest.mock import Mock
from app.main import can_access_google_page
import app.main

app.main.has_internet_connection = Mock()
app.main.valid_google_url = Mock()


def test_valid_url_and_connection_exists():
    app.main.has_internet_connection.return_value = True
    app.main.valid_google_url.return_value = True
    assert can_access_google_page("https://www.google.com/") == "Accessible"


def test_valid_url_and_connection_not_exists():
    app.main.has_internet_connection.return_value = False
    app.main.valid_google_url.return_value = True
    assert can_access_google_page("https://www.google.com/") == "Not accessible"


def test_bad_url_and_connection_exists():
    app.main.has_internet_connection.return_value = True
    app.main.valid_google_url.return_value = False
    assert can_access_google_page("https://www.lol.com/") == "Not accessible"


def test_bad_url_and_connection_not_exists():
    app.main.has_internet_connection.return_value = False
    app.main.valid_google_url.return_value = False
    assert can_access_google_page("https://www.lol.com/") == "Not accessible"


def test_empty_url_and_connection_exists():
    app.main.has_internet_connection.return_value = True
    app.main.valid_google_url.return_value = False
    assert can_access_google_page("") == "Not accessible"
