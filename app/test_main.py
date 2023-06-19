from typing import Any
from unittest.mock import patch
from app.main import can_access_google_page
from pytest import fixture


@fixture
def manager_fixture() -> Any:
    with (patch("app.main.valid_google_url") as valid_url,
          patch("app.main.has_internet_connection") as has_connection):
        yield valid_url, has_connection


def test_can_access_google_page(manager_fixture) -> None:
    valid_url, has_connection = manager_fixture
    valid_url.return_value = True
    has_connection.return_value = True
    action = can_access_google_page("https://www.google.com/")
    assert action == "Accessible"


def test_can_not_access_google_page_if_only_connection(manager_fixture) -> None:
    valid_url, has_connection = manager_fixture
    valid_url.return_value = False
    has_connection.return_value = True
    action = can_access_google_page("https://www.google.com/")
    assert action == "Not accessible"


def test_can_not_access_google_page_if_only_valid_url(manager_fixture) -> None:
    valid_url, has_connection = manager_fixture
    valid_url.return_value = True
    has_connection.return_value = False
    action = can_access_google_page("https://www.google.com/")
    assert action == "Not accessible"
