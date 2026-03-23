from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize("valid_url, internet_connection, expected_result",
                         [
                             (True, False, "Not accessible"),
                             (True, True, "Accessible"),
                             (False, True, "Not accessible"),
                             (False, False, "Not accessible"),
                         ]

                         )
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_return_true_when_url_is_valid_and_connection_exists(
        mocked_valid_google_url: bool,
        mocked_has_internet_connection: bool,
        valid_url: bool,
        internet_connection: bool,
        expected_result: str,

) -> None:
    mocked_valid_google_url.return_value = valid_url
    mocked_has_internet_connection.return_value = internet_connection

    result = can_access_google_page("https://google.com")

    assert result == expected_result
