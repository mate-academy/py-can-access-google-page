from unittest import mock
from app.main import can_access_google_page


def test_can_access__with_valid_url_and_internet() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=True),
         mock.patch("app.main.has_internet_connection", return_value=True)):
        assert can_access_google_page("https://www.google.com") == "Accessible"


def test_cannot_access__with_valid_url_and_without_internet() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=True),
         mock.patch("app.main.has_internet_connection", return_value=False)):
        assert can_access_google_page(
            "https://www.google.com"
        ) == "Not accessible"


def test_cannot_access__with_invalid_url_and_with_internet() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=False),
         mock.patch("app.main.has_internet_connection", return_value=True)):
        assert can_access_google_page(
            "https://wwwgoogle.com"
        ) == "Not accessible"


def test_cannot_access__with_unvalid_url_and_without_internet() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=False),
         mock.patch("app.main.has_internet_connection", return_value=False)):
        assert can_access_google_page(
            "https://wwwgoogle.com"
        ) == "Not accessible"
