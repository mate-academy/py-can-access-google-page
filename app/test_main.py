from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.fixture()
def url() -> str:
    return "https://www.google.com"


@pytest.fixture()
def has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as connection:
        yield connection


@pytest.fixture()
def valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as valid_url:
        yield valid_url


def test_should_call_has_internet_connection(
        url: str,
        has_internet_connection: mock
) -> None:
    can_access_google_page(url)
    has_internet_connection.assert_called_once()


def test_should_call_valid_google_url(
        url: str,
        valid_google_url: mock
) -> None:
    can_access_google_page(url)
    valid_google_url.assert_called_once()


@pytest.mark.parametrize(
    "has_connection, valid_value, result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ],
    ids=[
        "Url is incorrect",
        "Hasn't internet connection",
        "Url is incorrect and hasn't internet connection",
        "All the data is correct"
    ]
)
def test_should_be_accessible_if_has_connection_and_valid_url(
        has_internet_connection: mock,
        valid_google_url: mock,
        has_connection: bool,
        valid_value: bool,
        url: str,
        result: str
) -> None:
    has_internet_connection.return_value = has_connection
    valid_google_url.return_value = valid_value

    assert can_access_google_page(url) == result
