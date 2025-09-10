from unittest.mock import patch
from app.main import can_access_google_page


def test_accessible() -> None:
    with patch("app.main.has_internet_connection", return_value=True):
        with patch("app.main.valid_google_url",
                   return_value=True) as mock_valid:
            result = can_access_google_page("http://google.com")
            assert result == "Accessible"
            mock_valid.assert_called_once_with("http://google.com")


def test_not_accessible_invalid_url() -> None:
    with patch("app.main.has_internet_connection", return_value=True):
        with patch("app.main.valid_google_url",
                   return_value=False) as mock_valid:
            result = can_access_google_page("http://google.com")
            assert result == "Not accessible"
            mock_valid.assert_called_once_with("http://google.com")


def test_not_accessible_no_internet() -> None:
    with patch("app.main.has_internet_connection", return_value=False):
        with patch("app.main.valid_google_url",
                   return_value=True) as mock_valid:
            result = can_access_google_page("http://google.com")
            assert result == "Not accessible"
            mock_valid.assert_not_called()


def test_not_accessible_both_false() -> None:
    with patch("app.main.has_internet_connection", return_value=False):
        with patch("app.main.valid_google_url",
                   return_value=False) as mock_valid:
            result = can_access_google_page("http://google.com")
            assert result == "Not accessible"
            mock_valid.assert_not_called()
