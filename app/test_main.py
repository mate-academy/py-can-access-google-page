import pytest
from unittest import mock
from typing import Callable
from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") \
            as mocked_google_url:
        yield mocked_google_url


@pytest.fixture()
def mock_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") \
            as mocked_internet_connection:
        yield mocked_internet_connection


def test_allowed_access(mock_valid_google_url: Callable,
                        mock_has_internet_connection: Callable
                        ) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("valid_url") == "Accessible"


@pytest.mark.parametrize(
    "google_url, internet_connection, result",
    [
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_not_allowed_access_(mock_valid_google_url: Callable,
                             mock_has_internet_connection: Callable,
                             google_url: bool,
                             internet_connection: bool,
                             result: str
                             ) -> None:
    mock_valid_google_url.return_value = google_url
    mock_has_internet_connection.return_value = internet_connection
    assert can_access_google_page("invalid_url") == result
