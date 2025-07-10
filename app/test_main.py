from typing import Generator
from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocks() -> Generator[list[MagicMock], None, None]:
    with (
        mock.patch("app.main.valid_google_url")
        as mock_valid_google_url,
        mock.patch("app.main.has_internet_connection")
        as mock_has_internet_connection
    ):
        yield [mock_valid_google_url, mock_has_internet_connection]


def test_can_access_page_if_both_are_true(
        mocks: Generator[list[MagicMock], None, None]
) -> None:
    mocks[0].return_value = True
    mocks[1].return_value = True

    result = can_access_google_page("google.com")
    assert result == "Accessible"


def test_can_not_access_page_if_valid_url_is_false(
        mocks: Generator[list[MagicMock], None, None]
) -> None:
    mocks[0].return_value = False
    mocks[1].return_value = True

    result = can_access_google_page("google.com")
    assert result == "Not accessible"


def test_can_not_access_page_if_internet_connection_is_false(
        mocks: Generator[list[MagicMock], None, None]
) -> None:
    mocks[0].return_value = True
    mocks[1].return_value = False

    result = can_access_google_page("google.com")
    assert result == "Not accessible"


def test_can_not_access_page_if_both_are_false(
    mocks: Generator[list[MagicMock], None, None]
) -> None:
    mocks[0].return_value = False
    mocks[0].return_value = False

    result = can_access_google_page("google.com")
    assert result == "Not accessible"
