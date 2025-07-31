from unittest.mock import patch

from app.main import can_access_google_page


def test_both_true() -> None:
    with (patch("app.main.valid_google_url") as mock_valid_url,
         patch("app.main.has_internet_connection")
         as mock_has_internet_connection):

        mock_valid_url.return_value = True
        mock_has_internet_connection.return_value = True

        result = can_access_google_page("https://google.com")
        assert result == "Accessible"


def test_both_false() -> None:
    with (patch("app.main.valid_google_url") as mock_valid_url,
         patch("app.main.has_internet_connection")
         as mock_has_internet_connection):

        mock_valid_url.return_value = False
        mock_has_internet_connection.return_value = False

        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"


def test_with_only_internet_connection() -> None:
    with (patch("app.main.valid_google_url") as mock_valid_url,
         patch("app.main.has_internet_connection")
         as mock_has_internet_connection):

        mock_valid_url.return_value = False
        mock_has_internet_connection.return_value = True

        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"


def test_with_only_valid_url() -> None:
    with (patch("app.main.valid_google_url") as mock_valid_url,
         patch("app.main.has_internet_connection")
         as mock_has_internet_connection):

        mock_valid_url.return_value = True
        mock_has_internet_connection.return_value = False

        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"
