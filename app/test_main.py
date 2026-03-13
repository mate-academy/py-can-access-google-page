from unittest.mock import patch, Mock
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_returns_accessible_when_url_and_connection_are_valid(
    mock_valid_url: Mock,
    mock_internet: Mock
) -> None:
    mock_internet.return_value = True
    mock_valid_url.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_returns_not_accessible_when_url_is_invalid(
    mock_valid_url: Mock,
    mock_internet: Mock
) -> None:
    mock_internet.return_value = True
    mock_valid_url.return_value = False
    assert can_access_google_page("invalid-url") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_returns_not_accessible_when_no_internet_connection(
    mock_valid_url: Mock,
    mock_internet: Mock
) -> None:
    mock_internet.return_value = False
    mock_valid_url.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"
