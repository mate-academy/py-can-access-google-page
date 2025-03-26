import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_google_url() -> mock.MagicMock:
    with mock.patch("app.main.valid_google_url") as mocked_google_url:
        yield mocked_google_url


@pytest.fixture()
def mocked_internet_connection() -> mock.MagicMock:
    with (
        mock.patch("app.main.has_internet_connection")
        as mocked_internet_connection
    ):
        yield mocked_internet_connection


def test_valid_url_and_internet_connection_checked(
    mocked_google_url: mock.MagicMock,
    mocked_internet_connection: mock.MagicMock,
) -> None:
    can_access_google_page("url")
    mocked_google_url.assert_called_once_with("url")
    mocked_internet_connection.assert_called_once()


@pytest.mark.parametrize(
    "url_value,connection_value,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
    mocked_google_url: mock.MagicMock,
    mocked_internet_connection: mock.MagicMock,
    url_value: bool,
    connection_value: bool,
    expected: str,
) -> None:
    mocked_google_url.return_value = url_value
    mocked_internet_connection.return_value = connection_value
    assert can_access_google_page("") == expected
