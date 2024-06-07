from unittest.mock import patch

from app.main import can_access_google_page


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=True)
def test_check_access_page(mock_valid_google_url: patch,
                           mock_has_internet_connection: patch) -> None:
    assert can_access_google_page("https://www.google.com") == "Accessible"


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=False)
def test_check_invalid_url(mock_valid_google_url: patch,
                           mock_has_internet_connection: patch) -> None:
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=True)
def test_check_no_connection(mock_valid_google_url: patch,
                             mock_has_internet_connection: patch) -> None:
    assert can_acces_google_page("https://www.google.com") == "Not accessible"
