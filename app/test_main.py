from unittest import mock

from app.main import can_access_google_page


def test_can_access_google_page_true_state() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_google_url:
        with mock.patch("app.main.has_"
                        "internet_connection") as mocked_internet_connection:
            mocked_internet_connection.return_value = True
            mocked_google_url.return_value = True
            assert can_access_google_page("google.com") == "Accessible"


def test_can_access_google_page_without_internet_connection() -> None:
    with mock.patch("app.main.valid_"
                    "google_url") as mocked_google_url:
        with mock.patch("app.main.has_"
                        "internet_connection") as mocked_internet_connection:
            mocked_internet_connection.return_value = False
            mocked_google_url.return_value = True
            assert can_access_google_page("google.com") == "Not accessible"


def test_can_access_google_page_wit_invalid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_google_url:
        with mock.patch("app.main.has"
                        "_internet_connection") as mocked_internet_connection:
            mocked_internet_connection.return_value = True
            mocked_google_url.return_value = False
            assert can_access_google_page("google.com") == "Not accessible"
