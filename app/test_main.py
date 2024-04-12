from unittest import mock
from app import main


def test_check_can_access_google_page() -> None:
    main.valid_google_url = mock.MagicMock()
    main.has_internet_connection = mock.MagicMock()
    main.can_access_google_page("https://google.com")
    main.valid_google_url.assert_called_once()
    main.has_internet_connection.assert_called_once()
