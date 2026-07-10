from unittest import mock

from app.main import can_access_google_page


def test_returns_accessible_when_url_is_valid_and_internet_exists() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=True),
          mock.patch("app.main.has_internet_connection", return_value=True)):
        assert can_access_google_page("Mock") == "Accessible"


def test_no_access_when_there_is_no_internet() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=True),
          mock.patch("app.main.has_internet_connection", return_value=False)):
        assert can_access_google_page("Mock") == "Not accessible"


def test_no_access_when_the_url_is_incorrect() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=False),
          mock.patch("app.main.has_internet_connection", return_value=True)):
        assert can_access_google_page("Mock") == "Not accessible"
