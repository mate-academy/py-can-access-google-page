from unittest.mock import patch

from app.main import can_access_google_page


def test_can_access_google_page_valid_url_and_internet() -> None:
    with patch("app.main.valid_google_url",
               return_value=True) as mock_valid_url, \
         patch("app.main.has_internet_connection",
               return_value=True) as mock_internet:

        result = can_access_google_page("https://www.google.com")

        mock_valid_url.assert_called_once_with("https://www.google.com")
        mock_internet.assert_called_once()
        assert result == "Accessible"


def test_can_access_google_page_invalid_url() -> None:
    with patch("app.main.valid_google_url",
               return_value=False) as mock_valid_url, \
         patch("app.main.has_internet_connection",
               return_value=True) as mock_internet:

        result = can_access_google_page("https://www.google.com")

        mock_valid_url.assert_called_once_with("https://www.google.com")
        mock_internet.assert_called_once()
        assert result == "Not accessible"


def test_can_access_google_page_no_internet() -> None:
    with patch("app.main.has_internet_connection",
               return_value=False) as mock_internet:

        result = can_access_google_page("https://www.google.com")

        mock_internet.assert_called_once()
        assert result == "Not accessible"
