from unittest import mock
from app.main import can_access_google_page


def test_url_have_connection() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid, \
            mock.patch("app.main.has_internet_connection") as mock_connection:
        mocked_valid.return_value = True
        mock_connection.return_value = True
        result = can_access_google_page(url="https://www.google.com")
        assert result == "Accessible"


def test_url_have_no_connection() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid, \
            mock.patch("app.main.has_internet_connection") as mock_connection:
        mocked_valid.return_value = False
        mock_connection.return_value = False
        result = can_access_google_page(url="googgle.com")
        assert result == "Not accessible"
