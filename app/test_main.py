from unittest.mock import patch
from app.main import can_access_google_page


def mock_valid_google_url(url: str) -> bool:
    return True


def mock_has_internet_connection() -> bool:
    return True


@patch(
    "app.main.valid_google_url",
    side_effect=mock_valid_google_url)
@patch(
    "app.main.has_internet_connection",
    side_effect=mock_has_internet_connection)
def test_can_access_google_page_valid_url_and_internet(
        mock_valid_url: str,
        mock_internet_connection: int
) -> None:
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@patch(
    "app.main.valid_google_url",
    side_effect=mock_valid_google_url)
@patch(
    "app.main.has_internet_connection",
    return_value=False)
def test_can_access_google_page_valid_url_no_internet(
        mock_valid_url: str,
        mock_no_internet_connection: int
) -> None:
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@patch(
    "app.main.valid_google_url",
    return_value=False)
def test_can_access_google_page_invalid_url(mock_invalid_url: str) -> None:
    result = can_access_google_page("https://www.invalidurl.com")
    assert result == "Not accessible"
