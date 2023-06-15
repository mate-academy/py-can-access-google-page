from unittest import mock

from app.main import can_access_google_page


def test_can_access_google_page_accessible() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=True),
          mock.patch("app.main.has_internet_connection", return_value=True)):
        assert (can_access_google_page("https://www.google.com")
                == "Accessible")


def test_can_access_google_page_no_connection() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=True),
          mock.patch("app.main.has_internet_connection", return_value=False)):
        assert (can_access_google_page("https://www.google.com")
                == "Not accessible")


def test_can_access_google_page_invalid_url() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=False),
          mock.patch("app.main.has_internet_connection", return_value=True)):
        assert (can_access_google_page("https://www.example.com")
                == "Not accessible")


def test_can_access_google_page_no_connection_and_invalid_url() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=False),
          mock.patch("app.main.has_internet_connection", return_value=False)):
        assert (can_access_google_page("https://www.example.com")
                == "Not accessible")
