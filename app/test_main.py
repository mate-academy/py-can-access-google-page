from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_accessible_when_url_valid_and_internet_on(
    mock_has_internet_connection: bool,
    mock_valid_google_url: bool,
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_url_invalid(
    mock_valid_google_url: bool, mock_has_internet_connection: bool
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False

    assert can_access_google_page("https://not-google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_no_internet(
    mock_valid_google_url: bool, mock_has_internet_connection: bool
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True

    assert can_access_google_page("https://google.com") == "Not accessible"
