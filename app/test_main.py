from typing import Any
from unittest import mock
from unittest.mock import Mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_url() -> Any:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mocked_connection() -> Any:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_internet_connection(mocked_url: Mock,
                             mocked_connection: Mock) -> None:
    can_access_google_page("")
    mocked_connection.assert_called_once()


@pytest.mark.parametrize(
    "connection, url, result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Must return \'Accessible\' when all checks are True"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Must return \'Not accessible\' when no connection"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Must return \'Not accessible\' when url is incorrect"
        )
    ]
)
def test_can_access_google_page(
        mocked_url: Mock,
        mocked_connection: Mock,
        connection: bool,
        url: bool,
        result: str
) -> None:
    mocked_url.return_value = url
    mocked_connection.return_value = connection
    assert can_access_google_page("") == result
