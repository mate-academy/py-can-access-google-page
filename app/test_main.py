from unittest import mock

from app.main import can_access_google_page


def test_can_access_google_page_when_only_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid, \
            mock.patch("app.main.has_internet_connection") as mocked_connect:
        mocked_valid.return_value = True
        mocked_connect.return_value = False

        assert can_access_google_page("") == "Not accessible"


def test_can_access_google_page_when_all_checks_is_true() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid, \
            mock.patch("app.main.has_internet_connection") as mocked_connect:
        mocked_valid.return_value = True
        mocked_connect.return_value = True

        assert can_access_google_page("") == "Accessible"


def test_can_access_google_page_when_only_connection_is_true() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid, \
            mock.patch("app.main.has_internet_connection") as mocked_connect:
        mocked_valid.return_value = False
        mocked_connect.return_value = True

        assert can_access_google_page("") == "Not accessible"
