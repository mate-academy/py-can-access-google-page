import pytest

from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@pytest.fixture()
def mocked_internet() -> None:
    with mock.patch(
            "app.main.has_internet_connection"
    ) as mocked_internet_connection:
        yield mocked_internet_connection


@pytest.fixture()
def mocked_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url_check:
        yield mocked_url_check


@pytest.mark.parametrize(
    ("url,is_internet_connection,is_valid_url,result"),
    [
        ("http://youtube.com/", True, True, "Accessible"),
        ("you tube.com/", True, False, "Not accessible"),
        ("youtube.com/", False, True, "Not accessible")
    ],
    ids=[
        "good url and internet",
        "bad url",
        "no internet"
    ]
)
def test_can_access_google_page(
        mocked_internet: Callable,
        mocked_url: Callable,
        url: str,
        is_internet_connection: bool,
        is_valid_url: bool,
        result: str
) -> None:
    mocked_url.return_value = is_valid_url
    mocked_internet.return_value = is_internet_connection

    assert can_access_google_page(url) == result,\
        f"function should return {result}"
