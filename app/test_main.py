from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_accessible(mock_internet: bool, mock_valid_url:bool) -> None:
    assert can_access_google_page("https://www.google.com") == "Accessible"


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_no_internet(mock_internet: bool, mock_valid_url:bool) -> None:
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_invalid_url(mock_internet: bool, mock_valid_url:bool) -> None:
    assert can_access_google_page("https://wikipedia.org") == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=False)
def test_invalid_url_no_internet(mock_internet: bool, mock_valid_url:bool) -> None:
    assert can_access_google_page("https://wikipedia.org") == "Not accessible"
