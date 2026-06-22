from unittest import mock

from app.main import can_access_google_page


def test_accessible_when_valid_url_and_has_connection() -> None:
    with mock.patch("app.main.valid_google_url", return_value=True):
        with mock.patch("app.main.has_internet_connection", return_value=True):
            assert can_access_google_page("url") == "Accessible"


def test_not_accessible_when_invalid_url() -> None:
    with mock.patch("app.main.valid_google_url", return_value=False):
        with mock.patch("app.main.has_internet_connection", return_value=True):
            assert can_access_google_page("url") == "Not accessible"


def test_not_accessible_when_no_internet_connection() -> None:
    with mock.patch("app.main.valid_google_url", return_value=True):
        with mock.patch(
            "app.main.has_internet_connection", return_value=False
        ):
            assert can_access_google_page("url") == "Not accessible"
