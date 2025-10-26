from unittest.mock import patch
from app.main import can_access_google_page


url = "https://www.google.com"


def test_valid_url_and_true_connection() -> None:
    with (patch("app.main.valid_google_url",
                return_value=True),
          patch("app.main.has_internet_connection",
                return_value=True)):
        assert can_access_google_page(url) == "Accessible"


def test_not_valid_url_and_true_connection() -> None:
    with (patch("app.main.valid_google_url",
                return_value=False),
          patch("app.main.has_internet_connection",
                return_value=True)):
        assert can_access_google_page(url) == "Not accessible"


def test_valid_url_and_false_connection() -> None:
    with (patch("app.main.valid_google_url",
                return_value=True),
          patch("app.main.has_internet_connection",
                return_value=False)):
        assert can_access_google_page(url) == "Not accessible"


def test_not_valid_url_and_false_connection() -> None:
    with (patch("app.main.valid_google_url",
                return_value=False),
          patch("app.main.has_internet_connection",
                return_value=False)):
        assert can_access_google_page(url) == "Not accessible"
