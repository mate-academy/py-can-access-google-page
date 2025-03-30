from app.main import can_access_google_page
from unittest import TestCase
from unittest.mock import patch


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
class TestCanAccessGoogle(TestCase):

    def test_return_accessible_if_both_true(
            self, mock_validator: patch,
            mock_connection: patch
    ) -> None:
        mock_validator.return_value = True
        mock_connection.return_value = True
        assert can_access_google_page("test.url") == "Accessible"

    def test_return_not_accessible_if_url_not_valid(
            self, mock_validator: patch,
            mock_connection: patch
    ) -> None:
        mock_validator.return_value = False
        mock_connection.return_value = True
        assert can_access_google_page("test.url") == "Not accessible"

    def test_return_not_accessible_if_no_internet(
            self, mock_validator: patch,
            mock_connection: patch
    ) -> None:
        mock_validator.return_value = True
        mock_connection.return_value = False
        assert can_access_google_page("test.url") == "Not accessible"

    def test_return_not_accessible_if_both_false(
            self, mock_validator: patch,
            mock_connection: patch
    ) -> None:
        mock_validator.return_value = False
        mock_connection.return_value = False
        assert can_access_google_page("test.url") == "Not accessible"
