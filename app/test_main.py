from unittest import mock

from app.main import can_access_google_page


def test_valid_url_and_connection_exists() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url,\
         mock.patch("app.main.has_internet_connection") as mocked_connection:

        can_access_google_page(
            "https://mate.academy/learn?module=python-core&course=python"
        )

        mocked_valid_url.assert_called_once_with(
            "https://mate.academy/learn?module=python-core&course=python"
        )
        mocked_connection.assert_called_once()
