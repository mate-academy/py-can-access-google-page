from unittest import mock

from app import main


def test_should_return_not_accessible_for_invalid_url() -> None:
    with mock.patch("app.main.valid_google_url", return_value=False):
        with mock.patch("app.main.has_internet_connection", return_value=True):
            assert main.can_access_google_page("some url") == "Not accessible"


def test_should_return_not_accessible_for_wrong_time() -> None:
    with mock.patch("app.main.valid_google_url", return_value=True):
        with mock.patch("app.main.has_internet_connection",
                        return_value=False):
            assert main.can_access_google_page("some url") == "Not accessible"


def test_should_return_accessible_for_valid_url_and_time() -> None:
    with mock.patch("app.main.valid_google_url", return_value=True):
        with mock.patch("app.main.has_internet_connection", return_value=True):
            assert main.can_access_google_page("some url") == "Accessible"
