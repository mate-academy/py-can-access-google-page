from unittest import mock
from main import can_access_google_page


def test_can_access_google_page() -> None:
    with (mock.patch("main.has_internet_connection", return_value=True)
            as mock_internet,
            mock.patch("main.valid_google_url", return_value=True)
            as mock_url):
        result = can_access_google_page("https://www.google.com")

        mock_url.assert_called_once_with("https://www.google.com")
        mock_internet.assert_called_once()
        assert result == "Accessible"
