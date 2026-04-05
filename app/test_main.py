from typing import Generator
from unittest import mock


import pytest


from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_google_url() -> Generator:
    with (mock.patch("app.main.valid_google_url")
          as mocked_can_access_google_page):
        yield mocked_can_access_google_page


@pytest.fixture()
def mock_has_internet_connection() -> Generator:
    with (mock.patch("app.main.has_internet_connection")
          as mocked_has_internet_connection):
        yield mocked_has_internet_connection


@pytest.mark.parametrize(("return_is_valid, "
                          "return_has_connection, "
                          "expected_output"),
                         [
    (True, True, "Accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (False, False, "Not accessible")
])
def test_can_access_google_page(
        mock_has_internet_connection: mock.MagicMock,
        mock_valid_google_url: mock.MagicMock,
        return_is_valid: bool,
        return_has_connection: bool,
        expected_output: str
) -> None:
    mock_valid_google_url.return_value = return_is_valid
    mock_has_internet_connection.return_value = return_has_connection

    assert can_access_google_page("google.com") == expected_output
