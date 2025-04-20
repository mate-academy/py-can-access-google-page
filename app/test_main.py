import pytest

from typing import Generator
from app.main import can_access_google_page
from unittest.mock import patch


@pytest.fixture
def mocked_functions() -> Generator:
    with (patch("app.main.valid_google_url") as valid,
         patch("app.main.has_internet_connection") as internet):
        yield valid, internet


def test_can_access_google_page(
        mocked_functions: Generator
) -> None:
    valid, internet = mocked_functions
    valid.return_value = True
    internet.return_value = True

    assert can_access_google_page("google.com") == "Accessible"


def test_cant_access_with_url_false(
        mocked_functions: Generator
) -> None:
    valid, internet = mocked_functions
    valid.return_value = False
    internet.return_value = True

    assert can_access_google_page("google.com") == "Not accessible"


def test_cant_access_with_internet_false(
        mocked_functions: Generator
) -> None:
    valid, internet = mocked_functions
    valid.return_value = True
    internet.return_value = False

    assert can_access_google_page("google.com") == "Not accessible"
