from unittest import mock

from app.main import can_access_google_page


def test_can_access_google_page_when_all_conditions_true() -> None:
    with (
        mock.patch("app.main.valid_google_url") as mocked_valid,
        mock.patch("app.main.has_internet_connection") as mocked_has_connection
    ):
        mocked_valid.return_value = True
        mocked_has_connection.return_value = True
        assert can_access_google_page(
            "https://www.google.com/"
        ) == "Accessible"


def test_can_access_google_page_when_url_invalid() -> None:
    with (
        mock.patch("app.main.valid_google_url") as mocked_valid,
        mock.patch("app.main.has_internet_connection") as mocked_has_connection
    ):
        mocked_valid.return_value = False
        mocked_has_connection.return_value = True
        assert can_access_google_page(
            "https://www.goole.com/"
        ) == "Not accessible"


def test_can_access_google_page_when_no_internet() -> None:
    with (
        mock.patch("app.main.valid_google_url") as mocked_valid,
        mock.patch("app.main.has_internet_connection") as mocked_has_connection
    ):
        mocked_valid.return_value = True
        mocked_has_connection.return_value = False
        assert can_access_google_page(
            "https://www.google.com/"
        ) == "Not accessible"
        mocked_valid.assert_not_called()
