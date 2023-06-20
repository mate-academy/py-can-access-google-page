from typing import Any, Type
from unittest.mock import patch

import pytest

from app.main import can_access_google_page
from pytest import fixture


@fixture
def manager_fixture() -> Any:
    with (patch("app.main.valid_google_url") as valid_url,
          patch("app.main.has_internet_connection") as has_connection):
        yield valid_url, has_connection


@pytest.mark.parametrize(
    "url, connection, result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        manager_fixture: Type[fixture],
        url: bool,
        connection: bool,
        result: str
) -> None:
    valid_url, has_connection = manager_fixture
    valid_url.return_value = url
    has_connection.return_value = connection
    action = can_access_google_page("https://www.google.com/")
    assert action == result
