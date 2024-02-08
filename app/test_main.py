import pytest
import datetime
from unittest.mock import patch
from app import main  # assuming the functions are in main.py


def current_time() -> datetime.datetime:
    return datetime.datetime.now()


main.current_time = current_time


@pytest.fixture
def setup() -> tuple:
    url = "https://www.google.com"
    patch_valid_url = "app.main.valid_google_url"
    patch_has_connection = "app.main.has_internet_connection"
    with patch(patch_valid_url) as mock_valid_google_url, \
         patch(patch_has_connection) as mock_has_internet_connection:
        yield url, mock_valid_google_url, mock_has_internet_connection


test_params = [
    (True, True, "Accessible"),
    (False, True, "Not accessible"),
    (True, False, "Not accessible")
]


@pytest.mark.parametrize("valid_url, has_connection, expected", test_params)
def test_can_access_google_page(setup: tuple, valid_url: bool,
                                has_connection: bool, expected: str) -> None:
    url, mock_valid_google_url, mock_has_internet_connection = setup
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_connection
    result = main.can_access_google_page(url)
    assert result == expected
