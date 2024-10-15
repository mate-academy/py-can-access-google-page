from typing import Callable

import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


@pytest.fixture()
def mocked_has_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_has_connection:
        yield mock_has_connection


@pytest.mark.parametrize(
    "validation,connection,url,result",
    [
        pytest.param(
            False,
            False,
            "https://www.google.com.ua",
            "Not accessible",
            id="Should be NOT ACCESSIBLE when no connection and url not valid"
        ),
        pytest.param(
            True,
            False,
            "https://www.google.com.ua",
            "Not accessible",
            id="Should be NOT ACCESSIBLE when url not valid"
        ),
        pytest.param(
            False,
            True,
            "https://www.google.com.ua",
            "Not accessible",
            id="Should be NOT ACCESSIBLE when no connection"
        ),
        pytest.param(
            True,
            True,
            "https://www.google.com.ua",
            "Accessible",
            id="Should be ACCESSIBLE when connection and valid url"
        )]
)
def test_can_access_google_page(
        mocked_valid_url: Callable,
        mocked_has_connection: Callable,
        validation: bool,
        connection: bool,
        url: str,
        result: str
) -> None:
    mocked_valid_url.return_value = validation
    mocked_has_connection.return_value = connection
    assert can_access_google_page(url) == result


def test_valid_google_url_called(
        mocked_valid_url: Callable
) -> None:
    can_access_google_page("https://www.google.com.ua")
    mocked_valid_url.assert_called_once(), "Must be called once"


def test_has_internet_connection_called(
        mocked_has_connection: Callable
) -> None:
    can_access_google_page("https://www.google.com.ua")
    mocked_has_connection.assert_called_once(), "Must be called once"
