import pytest
from typing import Callable
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mocked_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_coonection:
        yield mocked_coonection


@pytest.mark.parametrize(
    "valid_url,connection,result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ],
    ids=[
        "You can't access the page if no internet connection",
        "You can't access the page if url not valid",
        "You can't access the page if no connection and url not valid",
        "You can access the page"
    ]
)
def test_can_access_google_page(
        mocked_valid_google_url: Callable,
        mocked_internet_connection: Callable,
        valid_url: bool,
        connection: bool,
        result: str
) -> None:
    mocked_valid_google_url.return_value = valid_url
    mocked_internet_connection.return_value = connection
    assert can_access_google_page("https://www.google.com/") == result
