from unittest import mock

from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url_check:
        with mock.patch(
                "app.main.has_internet_connection"
        ) as mocked_internet_check:
            can_access_google_page("1.1.1.1")
            mocked_url_check.assert_called_with("1.1.1.1")
            mocked_internet_check.assert_called()
