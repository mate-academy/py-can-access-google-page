from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page_accessible(
    mock_valid_google_url: MagicMock,
    mock_has_internet: MagicMock
) -> None:
    result: str = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page_no_internet(
    mock_valid_google_url: MagicMock,
    mock_has_internet: MagicMock
) -> None:
    result: str = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=False)
def test_can_access_google_page_invalid_url(
    mock_valid_google_url: MagicMock,
    mock_has_internet: MagicMock
) -> None:
    result: str = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=False)
def test_can_access_google_page_no_internet_and_invalid_url(
    mock_valid_google_url: MagicMock,
    mock_has_internet: MagicMock
) -> None:
    result: str = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
