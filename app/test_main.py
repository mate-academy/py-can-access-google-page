from unittest.mock import patch
from app.main import can_access_google_page


def test_is_accessible() -> None:
    url = "https://google.com"
    with patch("app.main.valid_google_url") as mock_valid_url:
        with patch("app.main.has_internet_connection") as mock_internet:
            mock_valid_url.return_value = True
            mock_internet.return_value = True
            assert can_access_google_page(url) == "Accessible"


def test_invalid_url() -> None:
    url = "https:/google.com"
    with patch("app.main.valid_google_url") as mock_valid_url:
        with patch("app.main.has_internet_connection") as mock_internet:
            mock_valid_url.return_value = False
            mock_internet.return_value = True
            assert can_access_google_page(url) == "Not accessible"


def test_no_internet() -> None:
    url = "https://google.com"
    with patch("app.main.valid_google_url") as mock_valid_url:
        with patch("app.main.has_internet_connection") as mock_internet:
            mock_valid_url.return_value = True
            mock_internet.return_value = False
            assert can_access_google_page(url) == "Not accessible"
