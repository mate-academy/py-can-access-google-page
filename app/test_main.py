from unittest import mock

from app.main import can_access_google_page


def test_inner_functions_should_be_called() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mocked_connection,
        mock.patch("app.main.valid_google_url") as mocked_valid_url
    ):

        can_access_google_page("url")
        mocked_connection.assert_called_once()
        mocked_valid_url.assert_called_once_with("url")


def test_should_return_accessible() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mocked_connection,
        mock.patch("app.main.valid_google_url") as mocked_valid_url
    ):
        mocked_connection.return_value = True
        mocked_valid_url.return_value = True

        assert can_access_google_page("url") == "Accessible"


def test_should_return_not_accessible() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mocked_connection,
        mock.patch("app.main.valid_google_url") as mocked_valid_url
    ):
        mocked_connection.return_value = True
        mocked_valid_url.return_value = False

        assert can_access_google_page("url") == "Not accessible"
