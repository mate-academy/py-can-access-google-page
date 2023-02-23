from unittest import TestCase
from unittest.mock import patch
from app.main import can_access_google_page
from typing import Callable


class TestAccess(TestCase):

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_is_accessible(
            self,
            mock_internet: Callable,
            mock_url: Callable
    ) -> None:
        mock_internet.return_value = True
        mock_url.return_value = True
        assert can_access_google_page("http://www.google.com") == "Accessible"

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_is_not_accessible_because_of_connection(
            self,
            mock_internet: Callable,
            mock_url: Callable
    ) -> None:
        mock_internet.return_value = False
        mock_url.return_value = True
        assert (can_access_google_page("http://www.google.com")
                == "Not accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_is_not_accessible_because_of_url(
            self,
            mock_internet: Callable,
            mock_url: Callable
    ) -> None:
        mock_internet.return_value = True
        mock_url.return_value = False
        assert (can_access_google_page("http://www.notgoogle.com")
                == "Not accessible")
