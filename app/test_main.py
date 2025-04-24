from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, valid_url, expected_result", [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Two functions return True",
        "No internet",
        "Invalid url",
        "No internet and invalid url"
    ]
)
def test_can_access_google_page_true(
        internet_connection: bool,
        valid_url: bool,
        expected_result: str
) -> None:
    with mock.patch("app.main.valid_google_url", return_value=valid_url), \
            mock.patch(
                "app.main.has_internet_connection",
                return_value=internet_connection
    ):
        assert can_access_google_page("") == expected_result
