from unittest import mock
import pytest
import requests
from typing import Any, Type
import datetime
from app.main import (
    valid_google_url,
    has_internet_connection,
    can_access_google_page
)


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        has_connection: mock.MagicMock,
        valid_url: mock.MagicMock
) -> None:
    can_access_google_page("url")
    has_connection.assert_called_once()
    valid_url.assert_called_once_with("url")


@pytest.mark.parametrize(
    "input_of_expected_url,expected_result",
    [
        pytest.param("https://cloud.google.com/", True, id="Working url"),
        pytest.param("https://httpbin.org/status/404", False, id="404 page")
    ]
)
def test_valid_google_url(
        input_of_expected_url: str,
        expected_result: bool
) -> None:
    assert valid_google_url(input_of_expected_url) == expected_result


@pytest.mark.parametrize(
    "argument,expected_error",
    [
        ("", requests.exceptions.MissingSchema)
    ]
)
def test_exceptions_valid_google_url(
        argument: Any,
        expected_error: Type[BaseException]
) -> None:
    with pytest.raises(expected_error):
        valid_google_url(argument)


def test_has_internet_connection() -> None:
    if datetime.datetime.now().hour in range(6, 23):
        expected_result = True
    else:
        expected_result = False
    assert has_internet_connection() == expected_result
