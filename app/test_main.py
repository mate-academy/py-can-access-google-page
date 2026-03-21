from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_when_all_conditions_met(
    mock_valid_url,
    mock_has_connection
):
    mock_valid_url.return_value = True
    mock_has_connection.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_cannot_access_google_page_when_url_invalid(
    mock_valid_url,
    mock_has_connection
):
    mock_valid_url.return_value = False
    mock_has_connection.return_value = True

    assert can_access_google_page("https://bing.com") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_cannot_access_google_page_when_no_internet(
    mock_valid_url,
    mock_has_connection
):
    mock_valid_url.return_value = True
    mock_has_connection.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_cannot_access_google_page_when_both_conditions_fail(
    mock_valid_url,
    mock_has_connection
):
    mock_valid_url.return_value = False
    mock_has_connection.return_value = False

    assert can_access_google_page("https://invalid.url") == "Not accessible"
