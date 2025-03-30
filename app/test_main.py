from app.main import can_access_google_page
from unittest.mock import patch
import pytest


@pytest.mark.parametrize("url, result", [
    ("https://mate.academy", "Accessible"),
    ("https://www.ukr.net/", "Accessible"),
    ("https://www.youtube.com/", "Accessible"),
    ("https://www.bing.com/", "Accessible")
])
def test_can_access_google_page(url: str, result: str) -> None:
    with patch("app.main.has_internet_connection") as mock_connect, \
         patch("app.main.valid_google_url") as mock_valid:
        mock_connect.return_value = True
        mock_valid.return_value = True
        assert can_access_google_page(url) == result


@pytest.mark.parametrize("url, result", [
    ("https://malte.academy", "Not accessible"),
    ("https://www.youtulbe.com/", "Not accessible"),
])
def test_can_access_not_google_page(url: str, result: str) -> None:
    with patch("app.main.has_internet_connection") as mock_connect, \
         patch("app.main.valid_google_url") as mock_valid:
        mock_connect.return_value = True
        mock_valid.return_value = False
        assert can_access_google_page(url) == result


def test_can_access_google_page_time() -> None:
    with patch("app.main.has_internet_connection") as mock_connect, \
         patch("app.main.valid_google_url") as mock_valid:
        mock_connect.return_value = False
        mock_valid.return_value = True
        assert can_access_google_page("google.com") == "Not accessible"
