from unittest.mock import patch

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet_connection,
    mock_valid_google_url,
):
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cannot_access_google_page_without_internet(
    mock_has_internet_connection,
    mock_valid_google_url,
):
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True

    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cannot_access_invalid_google_url(
    mock_has_internet_connection,
    mock_valid_google_url,
):
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False

    assert can_access_google_page("https://example.com") == "Not accessible"
