from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection_result, valid_result, expected_result", [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "test_valid_and_connection_true",
        "test_valid_false",
        "test_connection_false",
        "test_valid_and_connection_false"
    ]
)
def test_can_access_google_page(
        connection_result: bool,
        valid_result: bool,
        expected_result: str
) -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        with mock.patch("app.main.valid_google_url") as mocked_valid:
            mocked_valid.return_value = valid_result
            mocked_connection.return_value = connection_result

            assert (can_access_google_page("https://www.google.com.ua")
                    == expected_result)
