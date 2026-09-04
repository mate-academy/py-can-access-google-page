
from unittest import mock

from app import main


def test_accessible_if_connection_and_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_validation:
        mocked_validation.return_value = True

        with mock.patch("app.main.has_internet_connection") as mocked_internet:
            mocked_internet.return_value = True

            access_page = main.can_access_google_page(
                "https://www.google.com/"
            )

            assert access_page == "Accessible"


def test_not_accessible_if_no_connection_and_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_validation:
        mocked_validation.return_value = True

        with mock.patch("app.main.has_internet_connection") as mocked_internet:
            mocked_internet.return_value = False

            access_page = main.can_access_google_page(
                "https://www.google.com/"
            )

            assert access_page == "Not accessible"


def test_not_accessible_if_connection_and_invalid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_validation:
        mocked_validation.return_value = False

        with mock.patch("app.main.has_internet_connection") as mocked_internet:
            mocked_internet.return_value = True

            access_page = main.can_access_google_page(
                "https://www.google.com/"
            )

            assert access_page == "Not accessible"


def test_not_accessible_if_no_connection_and_invalid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_validation:
        mocked_validation.return_value = False

        with mock.patch("app.main.has_internet_connection") as mocked_internet:
            mocked_internet.return_value = False

            access_page = main.can_access_google_page(
                "https://www.google.com/"
            )

            assert access_page == "Not accessible"
