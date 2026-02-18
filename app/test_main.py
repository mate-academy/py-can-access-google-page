from unittest.mock import patch
from app.main import can_access_google_page


def test_google_double_true() -> None:
    with patch("app.main.valid_google_url") as mock_valid, \
         patch("app.main.has_internet_connection") as mock_connection:

        mock_valid.return_value = True
        mock_connection.return_value = True

        result = can_access_google_page("https://www.google.com/")

        assert result == "Accessible"


def test_google_conection_fasle() -> None:
    with patch("app.main.valid_google_url") as mock_valid, \
         patch("app.main.has_internet_connection") as mock_connection:

        mock_valid.return_value = True
        mock_connection.return_value = False

        result = can_access_google_page("https://www.google.com/")

        assert result == "Not accessible"


def test_google_url_invalid() -> None:
    with patch("app.main.valid_google_url") as mock_valid, \
         patch("app.main.has_internet_connection") as mock_connection:

        mock_valid.return_value = False
        mock_connection.return_value = True

        result = can_access_google_page("https://www.google.com/")

        assert result == "Not accessible"
