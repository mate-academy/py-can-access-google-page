from unittest.mock import patch, DEFAULT

import pytest

from app.main import can_access_google_page

MAGIC_URL = "magic URL"


@pytest.fixture
def mocked_funcs() -> dict:
    with patch.multiple(
        "app.main",
        has_internet_connection=DEFAULT,
        valid_google_url=DEFAULT
    ) as mocks:
        yield mocks


@pytest.mark.parametrize(
    "inet_conn_return, valid_url_return, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "if inet connection established and google url is valid",
        "if invalid googl url",
        "if no internet connection",
        "if no inet connection and google url is invalid",
    ]
)
def test_should_return_correct_value(
    mocked_funcs: dict,
    inet_conn_return: bool,
    valid_url_return: bool,
    expected: bool
) -> None:

    mocked_funcs["has_internet_connection"].return_value = inet_conn_return
    mocked_funcs["valid_google_url"].return_value = valid_url_return

    assert can_access_google_page(MAGIC_URL) == expected
