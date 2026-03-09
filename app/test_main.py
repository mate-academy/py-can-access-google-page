from unittest import mock
from app.main import can_access_google_page


def test_accessible_with_valid_url_and_connection() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=True),
          mock.patch("app.main.has_internet_connection", return_value=True)):
        assert can_access_google_page("https://google.com") == "Accessible"


def test_with_not_internet_connection() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=True),
          mock.patch("app.main.has_internet_connection", return_value=False)):
        assert can_access_google_page("https://google.com") == "Not accessible"


def test_with_invalid_url() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=False),
          mock.patch("app.main.has_internet_connection", return_value=True)):
        assert can_access_google_page("https://google.com") == "Not accessible"
