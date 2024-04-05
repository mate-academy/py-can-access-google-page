from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url_result,"
    "has_internet_connection_result,"
    "url,"
    "result",
    [
        (True, True, "https://www.google.com/", "Accessible"),
        (False, True, "https://www.googlefake.com/", "Not accessible"),
        (True, False, "https://www.google.com/", "Not accessible"),

    ]
)
def test_can_access_google_page(
        valid_google_url_result: bool,
        has_internet_connection_result: bool,
        url: str,
        result: str
) -> None:
    with (mock.patch("app.main.valid_google_url") as mocked_valid_google_url):
        mocked_valid_google_url.return_value = valid_google_url_result

        with (mock.patch("app.main.has_internet_connection")
              as mocked_has_internet_connection):
            return_value = has_internet_connection_result
            mocked_has_internet_connection.return_value = return_value

            assert can_access_google_page(url) == result
