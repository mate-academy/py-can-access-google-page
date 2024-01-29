import pytest

from unittest.mock import patch, Mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with patch("app.main.valid_google_url") as mock_google_url:
        yield mock_google_url


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with patch("app.main.has_internet_connection") as mock_internet_connection:
        yield mock_internet_connection


@pytest.mark.parametrize(
    "is_valid_url, is_exist_connection, result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "'Accessible' when url is valid and connection exist",
        "'Not accessible' when url isn't valid and connection exist",
        "'Not accessible' when url is valid and connection doesn't exist",
        "'Not accessible' when url isn't valid and connection doesn't exist",
    ]
)
def test_can_access_google_page(
        mocked_valid_google_url: Mock,
        mocked_has_internet_connection: Mock,
        is_valid_url: bool,
        is_exist_connection: bool,
        result: str,
) -> None:
    mocked_valid_google_url.return_value = is_valid_url
    mocked_has_internet_connection.return_value = is_exist_connection
    assert can_access_google_page("https://www.google.com.") == result
