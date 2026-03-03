from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_returns_accessible_when_url_is_valid_and_internet_is_connected(
    mock_internet: object, mock_valid_url: object
) -> None:
    result: str = can_access_google_page("https://google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_not_accessible_invalid_url(
    mock_internet: object, mock_valid_url: object
) -> None:
    result: str = can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_not_accessible_no_internet(
    mock_internet: object, mock_valid_url: object
) -> None:
    result: str = can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=False)
def test_not_accessible_both_fail(
    mock_internet: object, mock_valid_url: object
) -> None:
    result: str = can_access_google_page("https://google.com")
    assert result == "Not accessible"
