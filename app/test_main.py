from unittest import mock
from app.main import can_access_google_page


def test_correct_access() -> None:
    with (mock.patch("app.main.has_internet_connection", lambda: True),
          mock.patch("app.main.valid_google_url", lambda a: True)):
        assert can_access_google_page("some_url") == "Accessible"


def test_incorrect_access_has_not_internet_connection() -> None:
    with (mock.patch("app.main.has_internet_connection", lambda: False),
          mock.patch("app.main.valid_google_url", lambda a: True)):
        assert can_access_google_page("some_url") == "Not accessible"


def test_incorrect_access_invalid_google_url() -> None:
    with (mock.patch("app.main.has_internet_connection", lambda: True),
          mock.patch("app.main.valid_google_url", lambda a: False)):
        assert can_access_google_page("some_url") == "Not accessible"


def test_incorrect_access_no_internet_invalid_url() -> None:
    with (mock.patch("app.main.has_internet_connection", lambda: False),
          mock.patch("app.main.valid_google_url", lambda a: False)):
        assert can_access_google_page("some_url") == "Not accessible"
