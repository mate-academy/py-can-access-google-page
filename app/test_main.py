from unittest.mock import patch

from app.main import can_access_google_page


def test_try_to_access_google_page_with_incorrect_url() -> None:
    with (patch("app.main.valid_google_url") as mock_url,
          patch("app.main.has_internet_connection") as mock_connection):
        mock_url.return_value = False
        mock_connection.return_value = True
        assert can_access_google_page("www.testing.com") == "Not accessible"


def test_try_to_access_google_page_without_internet_connection() -> None:
    with (patch("app.main.valid_google_url") as mock_url,
          patch("app.main.has_internet_connection") as mock_connection):
        mock_url.return_value = True
        mock_connection.return_value = False
        assert can_access_google_page("www.testing.com") == "Not accessible"


def test_try_to_access_with_incorrect_url_and_without_internet_connection() \
        -> None:
    with (patch("app.main.valid_google_url") as mock_url,
          patch("app.main.has_internet_connection") as mock_connection):
        mock_url.return_value = False
        mock_connection.return_value = False
        assert can_access_google_page("www.testing.com") == "Not accessible"


def test_try_to_access_google_with_valid_url_and_with_internet_connection() \
        -> None:
    with (patch("app.main.valid_google_url") as mock_url,
          patch("app.main.has_internet_connection") as mock_connection):
        mock_url.return_value = True
        mock_connection.return_value = True
        assert can_access_google_page("www.testing.com") == "Accessible"
