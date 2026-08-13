from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(
    mock_valid_google_url: patch,
    mock_has_internet_connection: patch,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_url_and_no_connection(
    mock_valid_google_url: patch,
    mock_has_internet_connection: patch,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_url_and_connection_exists(
    mock_valid_google_url: patch,
    mock_has_internet_connection: patch,
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    assert can_access_google_page(
        "https://invalid-url.com") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_url_and_no_connection(
    mock_valid_google_url: patch,
    mock_has_internet_connection: patch,
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False

    assert (
        can_access_google_page("https://invalid-url.com") == "Not accessible"
    )
