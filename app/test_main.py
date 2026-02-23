from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=True),
          mock.patch("app.main.has_internet_connection", return_value=True)):
        assert can_access_google_page("https://google.com") == "Accessible"

    with (mock.patch("app.main.valid_google_url", return_value=True),
          mock.patch("app.main.has_internet_connection", return_value=False)):
        assert can_access_google_page("https://google.com") == "Not accessible"

    with (mock.patch("app.main.valid_google_url", return_value=False),
          mock.patch("app.main.has_internet_connection", return_value=True)):
        assert can_access_google_page("Hello") == "Not accessible"

    with (mock.patch("app.main.valid_google_url", return_value=False),
          mock.patch("app.main.has_internet_connection", return_value=False)):
        assert can_access_google_page("hello") == "Not accessible"
