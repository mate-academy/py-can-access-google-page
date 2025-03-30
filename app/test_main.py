from unittest.mock import patch

import app.main
from app.main import can_access_google_page


def test_can_access_google_page_accessible():
    with patch(
            "app.main.valid_google_url", return_value=True
    ), patch(
        "app.main.has_internet_connection", return_value=True
    ):
        assert can_access_google_page("https://www.google.com") == "Accessible"


def test_can_access_google_page_invalid_url():
    with patch(
            "app.main.valid_google_url", return_value=False
    ), patch(
        "app.main.has_internet_connection", return_value=True
    ):
        assert can_access_google_page("https://invalid-url.com") == "Not accessible"


def test_can_access_google_page_no_internet():
    with patch(
            "app.main.valid_google_url", return_value=True
    ), patch(
        "app.main.has_internet_connection", return_value=False
    ):
        assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_can_access_google_page_both_invalid():
    with patch(
            "app.main.valid_google_url", return_value=False
    ), patch(
        "app.main.has_internet_connection", return_value=False
    ):
        assert can_access_google_page("https://www.google.com") == "Not accessible"
