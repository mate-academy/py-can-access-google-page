from unittest import mock
from app.main import can_access_google_page


def test_functions_were_called() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url, \
            mock.patch("app.main.has_internet_connection") as mocked_internet:
        mocked_url.return_value = True
        mocked_internet.return_value = True
        can_access_google_page("http://google.com")
        mocked_url.assert_called_once()
        mocked_internet.assert_called_once()
