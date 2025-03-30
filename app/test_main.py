from __future__ import annotations
import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_link, has_internet_connection, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_url: mock.Mock,
                                mocked_internet_connection: mock.Mock,
                                valid_link: bool,
                                has_internet_connection: bool,
                                expected_result: str) -> None:

    mocked_url.return_value = valid_link
    mocked_internet_connection.return_value = has_internet_connection
    assert can_access_google_page("https://www.google.com") == expected_result
