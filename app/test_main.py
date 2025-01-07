from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page_accessible() -> None:
    """
    Test: valid URL and internet connection.
    Expected result: returns "Accessible".
    """
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://www.google.com")
        assert result == "Accessible", (
            "Expected 'Accessible', but the result is different."
        )


def test_can_access_google_page_no_internet() -> None:
    """
    Test: valid URL, but no internet connection.
    Expected result: returns "Not accessible"
    """
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible", (
            "Expected 'Not accessible', but the result is different."
        )


def test_can_access_google_page_invalid_url() -> None:
    """
    Test: Invalid URL, but internet connection is present.
    Expected result: "Not accessible" is returned.
    """
    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://invalid-url.com")
        assert result == "Not accessible", (
            "Expected 'Not accessible', but the result is different."
        )


def test_can_access_google_page_invalid_url_no_internet() -> None:
    """
    Test: Invalid URL and no internet connection.
    Expected result: "Not accessible" is returned.
    """
    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://invalid-url.com")
        assert result == "Not accessible", (
            "Expected 'Not accessible', but the result is different."
        )
