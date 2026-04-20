from unittest import mock

from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with mock.patch("app.main.valid_google_url") as mock_url:
        mock_url.return_value = True
        with mock.patch("app.main.has_internet_connection") as mock_conn:
            mock_conn.return_value = True
            result = can_access_google_page(url="https://test.com")
            assert result == "Accessible"

    with mock.patch("app.main.valid_google_url") as mock_url:
        mock_url.return_value = False
        with mock.patch("app.main.has_internet_connection") as mock_conn:
            mock_conn.return_value = False
            result = can_access_google_page(url="https://test.com")
            assert result == "Not accessible"

    with mock.patch("app.main.valid_google_url") as mock_url:
        mock_url.return_value = True
        with mock.patch("app.main.has_internet_connection") as mock_conn:
            mock_conn.return_value = False
            result = can_access_google_page(url="https://test.com")
            assert result == "Not accessible"

    with mock.patch("app.main.valid_google_url") as mock_url:
        mock_url.return_value = False
        with mock.patch("app.main.has_internet_connection") as mock_conn:
            mock_conn.return_value = True
            result = can_access_google_page(url="https://test.com")
            assert result == "Not accessible"
