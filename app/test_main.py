from unittest.mock import MagicMock, patch
from app.main import can_access_google_page

url = "https://www.notavalidurl.com"


def test_can_access_google_page_access_granted() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=True):
        assert can_access_google_page(url) == "Accessible"


def test_can_access_google_page_no_internet() -> None:
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=True):
        assert can_access_google_page(url) == "Not accessible"


def test_can_access_google_page_invalid_url() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=False):
        assert can_access_google_page(url) == "Not accessible"


def test_cannot_access_if_both_connection_and_valid_url_are_false() -> None:
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=False):
        assert can_access_google_page(url) == "Not accessible"


def test_cannot_access_if_only_connection() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=False):
        assert can_access_google_page(url) == "Not accessible"


def test_cannot_access_if_only_valid_url() -> None:
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=True):
        assert can_access_google_page(url) == "Not accessible"


def test_connection_and_valid_url_are_true() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=True):
        assert can_access_google_page(url) == "Accessible"
