from unittest import mock

from app.main import (
    can_access_google_page
)


def test_valid_url_and_connection_exists_returns_accessible() -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid, \
         mock.patch("app.main.has_internet_connection") as mock_internet:
        mock_valid.return_value = True
        mock_internet.return_value = True
        result = can_access_google_page("http://google.com")
        assert result == "Accessible"


def test_invalid_url_returns_not_accessible() -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid, \
         mock.patch("app.main.has_internet_connection") as mock_internet:
        mock_valid.return_value = False
        mock_internet.return_value = True
        result = can_access_google_page("http://google.com")
        assert result == "Not accessible"


def test_no_connection_returns_not_accessible() -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid, \
         mock.patch("app.main.has_internet_connection") as mock_internet:
        mock_valid.return_value = True
        mock_internet.return_value = False
        result = can_access_google_page("http://google.com")
        assert result == "Not accessible"
