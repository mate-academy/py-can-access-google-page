from unittest.mock import patch

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(mock_internet, mock_valid_url):
    mock_internet.return_value = True
    mock_valid_url.return_value = True

    actual_result = can_access_google_page("https://google.com")

    assert actual_result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_invalid_url(mock_internet, mock_valid_url):
    mock_internet.return_value = True
    mock_valid_url.return_value = False

    actual_result = can_access_google_page("https://google.com")

    assert actual_result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_no_internet(mock_internet, mock_valid_url):
    mock_internet.return_value = False
    mock_valid_url.return_value = True

    actual_result = can_access_google_page("https://google.com")

    assert actual_result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_not_accessible(mock_internet, mock_valid_url):
    mock_internet.return_value = False
    mock_valid_url.return_value = False

    actual_result = can_access_google_page("https://google.com")

    assert actual_result == "Not accessible"
