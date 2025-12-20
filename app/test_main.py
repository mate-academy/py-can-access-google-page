from unittest import mock
from app.main import can_access_google_page


def test_valid_url_and_connection_exists() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid, \
            mock.patch("app.main.has_internet_connection") as mock_connection:
        result = can_access_google_page(url="https://www.google.com")
        mocked_valid.assert_called_once()
        mock_connection.assert_called_once()
        assert result == "Accessible"
