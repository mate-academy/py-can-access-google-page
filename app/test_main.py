from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,internet_connection,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        valid_url: bool,
        internet_connection: bool,
        expected: str
) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        mocked_url.return_value = valid_url

        with mock.patch("app.main.has_internet_connection") as mocked_internet:
            mocked_internet.return_value = internet_connection

            assert can_access_google_page("https://www.google.com") == expected
