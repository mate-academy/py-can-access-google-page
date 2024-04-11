from typing import Any
import unittest.mock
from pytest import fixture

import app.main


@fixture()
def mocked_valid_url() -> Any:
    with unittest.mock.patch("app.main.valid_google_url") as filler1:
        filler1.return_value = True
        yield filler1


@fixture()
def mocked_has_connection() -> Any:
    with unittest.mock.patch("app.main.has_internet_connection") as filler2:
        filler2.return_value = True
        yield filler2


def test_functions_called_properly(
        mocked_valid_url: Any,
        mocked_has_connection: Any
) -> None:
    app.main.can_access_google_page("google.com")
    mocked_has_connection.assert_called_once()
    mocked_valid_url.assert_called_once_with("google.com")


def test_everything_valid(
    mocked_valid_url: Any,
    mocked_has_connection: Any
) -> None:
    assert app.main.can_access_google_page("google.com") == "Accessible"


def test_only_valid_url(
        mocked_valid_url: Any,
        mocked_has_connection: Any
) -> None:
    mocked_has_connection.return_value = False
    assert app.main.can_access_google_page("google.com") == "Not accessible"


def test_only_valid_connection(
        mocked_valid_url: Any,
        mocked_has_connection: Any
) -> None:
    mocked_valid_url.return_value = False
    assert app.main.can_access_google_page("google..com") == "Not accessible"
