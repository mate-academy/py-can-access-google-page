from unittest import mock
from app.main import can_access_google_page


def test_can_access() -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid_url,\
            mock.patch("app.main.has_internet_connection") as mock_internet_connection:
            mock_valid_url.return_value = True
            mock_internet_connection.return_value = True
            assert can_access_google_page("url") == "Accessible"

def test_cannot_access_without_internet_connection() -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid_url,\
            mock.patch("app.main.has_internet_connection") as mock_internet_connection:
            mock_valid_url.return_value = True
            mock_internet_connection.return_value = False
            assert can_access_google_page("url") == "Not accessible"


def test_cannot_access_invalid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid_url,\
            mock.patch("app.main.has_internet_connection") as mock_internet_connection:
            mock_valid_url.return_value = False
            mock_internet_connection.return_value = True
            assert can_access_google_page("url") == "Not accessible"


def test_both_internet_connection_and_url_valid_are_false() -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid_url,\
            mock.patch("app.main.has_internet_connection") as mock_internet_connection:
            mock_valid_url.return_value = False
            mock_internet_connection.return_value = False
            assert can_access_google_page("url") == "Not accessible"