from app.main import can_access_google_page

from unittest import mock

import pytest


@pytest.fixture()
def test_mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_function:
        yield mock_function


@pytest.fixture()
def test_mocked_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_function:
        yield mocked_function


def test_can_access_google_page(
        test_mocked_valid_google_url: str,
        test_mocked_has_internet_connection: str
) -> None:
    test_mocked_valid_google_url.return_value = True
    test_mocked_has_internet_connection.return_value = False
    assert (can_access_google_page(test_mocked_valid_google_url)
            == "Not accessible")


def test_can_access_google_page_not_accessible(
        test_mocked_valid_google_url: str,
        test_mocked_has_internet_connection: str
) -> None:
    test_mocked_valid_google_url.return_value = False
    test_mocked_has_internet_connection.return_value = True
    assert (can_access_google_page(test_mocked_valid_google_url)
            == "Not accessible")
