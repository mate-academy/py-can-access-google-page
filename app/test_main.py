import unittest
from unittest.mock import patch, MagicMock


from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
class TestCanAccessGooglePage(unittest.TestCase):
    def test_access_google_page(
            self,
            mock_url: MagicMock,
            mock_internet: MagicMock
    ) -> None:
        mock_url.return_value = True
        mock_internet.return_value = True
        assert (can_access_google_page("https://www.google.com")
                == "Accessible")

    def test_access_google_page_with_invalid_url(
            self,
            mock_url: MagicMock,
            mock_internet: MagicMock
    ) -> None:
        mock_url.return_value = False
        mock_internet.return_value = True
        assert (can_access_google_page("https://www.google.com")
                == "Not accessible")

    def test_access_google_page_without_internet_connection(
            self,
            mock_url: MagicMock,
            mock_internet: MagicMock
    ) -> None:
        mock_url.return_value = True
        mock_internet.return_value = False
        assert (can_access_google_page("https://www.google.com")
                == "Not accessible")

    def test_access_without_valid_url_and_internet_connection(
            self,
            mock_url: MagicMock,
            mock_internet: MagicMock
    ) -> None:
        mock_url.return_value = False
        mock_internet.return_value = False
        assert (can_access_google_page("https://www.google.com")
                == "Not accessible")
