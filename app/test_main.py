from unittest.mock import patch

from app.main import can_access_google_page


def test_accesability_with_no_connection() -> None:
    with patch("app.main.has_internet_connection", return_value=False) as mock_connection:
        response = can_access_google_page("https://www.google.com")

        mock_connection.assert_called_once()

        assert response == "Not accessible"


def test_accesability_without_valid_url_and_good_connection() -> None:
    with patch("app.main.valid_google_url", return_value=False) as mock_url, \
            patch("app.main.has_internet_connection", return_value=True) as mock_connection:
        response = can_access_google_page("https://www.google.com")

        mock_url.assert_called_once_with("https://www.google.com")
        mock_connection.assert_called_once()

        assert response == "Not accessible"


def test_accesability_with_valid_url_and_good_connection() -> None:
    with patch("app.main.valid_google_url", return_value=True) as mock_url, \
            patch("app.main.has_internet_connection", return_value=True) as mock_connection:
        response = can_access_google_page("https://www.google.com")

        mock_url.assert_called_once_with("https://www.google.com")
        mock_connection.assert_called_once()

        assert response == "Accessible"
