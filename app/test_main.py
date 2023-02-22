from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page_access_granted(mock_valid_url: str,
                                               mock_internet: str) -> None:
    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == "Accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page_no_internet(mock_valid_url: str,
                                            mock_internet: str) -> None:
    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=False)
def test_can_access_google_page_invalid_url(mock_valid_url: str,
                                            mock_internet: str) -> None:
    url = "https://www.notavalidurl.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"
