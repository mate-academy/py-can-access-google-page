import pytest

from app.main import can_access_google_page
from unittest import mock
from typing import Callable


@pytest.mark.parametrize(
    "url, connection, expected",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Accessible",
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Not accessible when no internet connection",
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Not accessible when invalid url",
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="Not accessible when invalid url and no internet connection",
        )
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_valid_googl_url: Callable,
        mocked_has_internet_connection: Callable,
        url: bool,
        connection: bool,
        expected: str
) -> None:
    mocked_valid_googl_url.return_value = url
    mocked_has_internet_connection.return_value = connection
    assert can_access_google_page("http://google.com") == expected
