from typing import Any
from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import can_access_google_page


URL = "https://www.google.com/"


@pytest.fixture()
def mocked_valid_google_url(request: Any) -> MagicMock:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        mocked_url.return_value = request.param
        yield mocked_url


@pytest.fixture()
def mocked_has_internet_connection(request: Any) -> MagicMock:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        mocked_connection.return_value = request.param
        yield mocked_connection


@pytest.mark.parametrize(
    "mocked_valid_google_url, mocked_has_internet_connection, expected_result",
    [
        pytest.param(
            False,
            False,
            "Not accessible"
        ),
        pytest.param(
            True,
            False,
            "Not accessible"
        ),
        pytest.param(
            False,
            True,
            "Not accessible"
        ),
        pytest.param(
            True,
            True,
            "Accessible"
        ),
    ],
    indirect=["mocked_valid_google_url", "mocked_has_internet_connection"]
)
def test_can_access_google_page(
        mocked_valid_google_url: mock,
        mocked_has_internet_connection: mock,
        expected_result: str
) -> None:
    assert can_access_google_page(URL) == expected_result
