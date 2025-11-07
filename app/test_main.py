from unittest import mock

from app.main import can_access_google_page

valid_url = "https://google.com"
invalid_url = "https://fake.com"

def test_can_access_google_page() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=True),
         mock.patch("app.main.has_internet_connection", return_value=True)):

        assert can_access_google_page(valid_url) == "Accessible"


def test_can_access_google_page_not_accessible_invalid_url() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=False),
         mock.patch("app.main.has_internet_connection", return_value=True)):

        assert can_access_google_page(invalid_url) == "Not accessible"


def test_can_access_google_page_not_accessible_no_internet() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=True),
         mock.patch("app.main.has_internet_connection", return_value=False)):

        assert can_access_google_page(valid_url) == "Not accessible"


def test_can_access_to_page_no_internet_and_fake_page() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=False),
            mock.patch("app.main.has_internet_connection", return_value=False)):
        assert can_access_google_page(valid_url) == "Not accessible"
