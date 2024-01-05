from unittest import mock
import app.main


def test_can_access_google_page_all_true() -> None:
    with mock.patch(
            "app.main.valid_google_url"
    ) as mocked_valid_google_url:
        with mock.patch(
                "app.main.has_internet_connection"
        ) as mocked_has_internet_connection:
            mocked_valid_google_url.return_value = True
            mocked_has_internet_connection.return_value = True
            assert app.main.can_access_google_page(
                "google.com"
            ) == "Accessible"


def test_can_access_google_page_url_false() -> None:
    with mock.patch(
            "app.main.valid_google_url"
    ) as mocked_valid_google_url:
        with mock.patch(
                "app.main.has_internet_connection"
        ) as mocked_has_internet_connection:
            mocked_valid_google_url.return_value = False
            mocked_has_internet_connection.return_value = True
            assert app.main.can_access_google_page(
                "google.com"
            ) == "Not accessible"


def test_can_access_google_page_internet_connection_false() -> None:
    with mock.patch(
            "app.main.valid_google_url"
    ) as mocked_valid_google_url:
        with mock.patch(
                "app.main.has_internet_connection"
        ) as mocked_has_internet_connection:
            mocked_valid_google_url.return_value = True
            mocked_has_internet_connection.return_value = False
            assert app.main.can_access_google_page(
                "google.com"
            ) == "Not accessible"
