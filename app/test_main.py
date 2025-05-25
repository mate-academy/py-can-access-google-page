from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_success(
        mock_valid_url: bool,
        mock_has_internet: bool
) -> None:
    mock_has_internet.return_value = True
    mock_valid_url.return_value = True
    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_url_returns_not_accessible(
        mock_valid_url: bool,
        mock_has_internet: bool
) -> None:
    mock_has_internet.return_value = True
    mock_valid_url.return_value = False
    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_no_internet_returns_not_accessible(
        mock_valid_url: bool,
        mock_has_internet: bool
) -> None:
    mock_has_internet.return_value = False
    mock_valid_url.return_value = True
    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_both_checks_fail_returns_not_accessible(
        mock_valid_url: bool,
        mock_has_internet: bool
) -> None:
    mock_has_internet.return_value = False
    mock_valid_url.return_value = False
    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"
