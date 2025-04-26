from unittest import mock

from app.main import can_access_google_page


def test_can_access_google_page_accessible() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=True):
        with mock.patch("app.main.valid_google_url", return_value=True):
            result = can_access_google_page("https://www.google.com")
            assert result == "Accessible"


def test_can_access_google_page_not_accessible_due_to_internet() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=False):
        with mock.patch("app.main.valid_google_url", return_value=True):
            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"


def test_can_access_google_page_not_accessible_due_to_invalid_url() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=True):
        with mock.patch("app.main.valid_google_url", return_value=False):
            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"


def test_can_access_google_page_when_both_invalid() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=False):
        with mock.patch("app.main.valid_google_url", return_value=False):
            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"
