from unittest import mock

from app.main import can_access_google_page


def test_functions_have_called() -> None:
    with (mock.patch("app.main.valid_google_url") as mocked_valid,
         mock.patch("app.main.has_internet_connection") as mocked_has_conn):
        can_access_google_page("http://www.google.com")
        mocked_valid.assert_called_once_with("http://www.google.com")
        mocked_has_conn.assert_called_once()
