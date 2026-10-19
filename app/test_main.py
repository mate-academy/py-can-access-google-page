from unittest.mock import patch

from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_accessible(
    mock_valid_google_url,
    mock_has_internet_connection,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_invalid_url(
    mock_valid_google_url,
    mock_has_internet_connection,
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    assert can_access_google_page("https://invalid.com") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_no_internet(
    mock_valid_google_url,
    mock_has_internet_connection,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_invalid_url_and_no_internet(
    mock_valid_google_url,
    mock_has_internet_connection,
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False

    assert can_access_google_page("https://invalid.com") == "Not accessible"
