from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=True)
def test_valid_url_and_connection_exists(
        mock_valid_google_url: bool,
        mock_has_internet_connection: bool
) -> None:
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=False)
def test_invalid_url_connection_exists(
        mock_valid_google_url: bool,
        mock_has_internet_connection: bool
) -> None:
    result = can_access_google_page("https://badsite.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=True)
def test_valid_url_no_connection(
        mock_valid_google_url: bool,
        mock_has_internet_connection: bool
) -> None:
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=False)
def test_invalid_url_no_connection(
        mock_valid_google_url: bool,
        mock_has_internet_connection: bool
) -> None:
    result = can_access_google_page("https://badsite.com")
    assert result == "Not accessible"
