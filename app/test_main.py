from unittest import mock
from main import can_access_google_page


def test_can_access_google_page_both_true() -> None:
    with (mock.patch("main.has_internet_connection", return_value=True) as mock_internet,
          mock.patch("main.valid_google_url", return_value=True) as mock_url):
        result = can_access_google_page("https://www.google.com")

        mock_url.assert_called_once_with("https://www.google.com")
        mock_internet.assert_called_once()
        assert result == "Accessible"


def test_can_access_google_page_no_internet() -> None:
    with (mock.patch("main.has_internet_connection", return_value=False) as mock_internet,
          mock.patch("main.valid_google_url", return_value=True) as mock_url):
        result = can_access_google_page("https://www.google.com")

        mock_internet.assert_called_once()
        assert result == "Not accessible"


def test_can_access_google_page_invalid_url() -> None:
    with (mock.patch("main.has_internet_connection", return_value=True) as mock_internet,
          mock.patch("main.valid_google_url", return_value=False) as mock_url):
        result = can_access_google_page("https://www.google.com")

        mock_url.assert_called_once_with("https://www.google.com")
        mock_internet.assert_called_once()
        assert result == "Not accessible"


def test_can_access_google_page_both_false() -> None:
    with (mock.patch("main.has_internet_connection", return_value=False) as mock_internet,
          mock.patch("main.valid_google_url", return_value=False) as mock_url):
        result = can_access_google_page("https://www.google.com")

        mock_internet.assert_called_once()
        assert result == "Not accessible"