from unittest import mock

from app.main import can_access_google_page


def test_accessible_when_has_internet_and_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        with mock.patch("app.main.has_internet_connection") as mocked_internet:
            mocked_valid_url.return_value = True
            mocked_internet.return_value = True

            assert can_access_google_page("google.com/") == "Accessible"


def test_not_accessible_when_no_valid_url_and_no_internet() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        with mock.patch("app.main.has_internet_connection") as mocked_internet:
            mocked_valid_url.return_value = False
            mocked_internet.return_value = False

            assert can_access_google_page("google.com/") == "Not accessible"


def test_not_accessible_when_valid_url_and_no_internet() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        with mock.patch("app.main.has_internet_connection") as mocked_internet:
            mocked_valid_url.return_value = True
            mocked_internet.return_value = False

            assert can_access_google_page("google.com/") == "Not accessible"


def test_not_accessible_when_has_internet_and_no_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        with mock.patch("app.main.has_internet_connection") as mocked_internet:
            mocked_valid_url.return_value = False
            mocked_internet.return_value = True

            assert can_access_google_page("google.com/") == "Not accessible"
