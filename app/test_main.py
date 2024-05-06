import pytest
from typing import Callable
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "expected_google_url,"
    "expected_internet_connection, "
    "expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "with valid url and internet connection",
        "with non-correct url",
        "without internet connection",
        "with non-correct url and without internet"
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_google_url: Callable,
        mocked_internet_connection: Callable,
        expected_google_url: bool,
        expected_internet_connection: bool,
        expected_result: str
) -> None:
    mocked_google_url.return_value = expected_google_url
    mocked_internet_connection.return_value = expected_internet_connection
    result = can_access_google_page("https://www.google.com")
    assert result == expected_result
