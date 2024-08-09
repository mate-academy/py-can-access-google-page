from unittest import mock
from app.main import can_access_google_page


def test_would_return_accessible_when_internet_and_valid_true() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=True),
          mock.patch("app.main.has_internet_connection", return_value=True)):
        assert (
            can_access_google_page("1") == "Accessible"
        ), f"Expected 'Accessible' but was {can_access_google_page("1")}"


def test_would_return_not_accessible_when_only_valid_true() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=False),
          mock.patch("app.main.has_internet_connection", return_value=True)):
        assert (
            can_access_google_page("1") == "Not accessible"
        ), f"Expected 'Not accessible' but was {can_access_google_page("1")}"


def test_would_return_not_accessible_when_only_connect_true() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=True),
          mock.patch("app.main.has_internet_connection", return_value=False)):
        assert (
            can_access_google_page("1") == "Not accessible"
        ), f"Expected 'Not accessible' but was {can_access_google_page("1")}"
