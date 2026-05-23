import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_connection() -> None:
    with (
        mock.patch("app.main.valid_google_url")
        as mock_test_valid_url,
        mock.patch("app.main.has_internet_connection")
        as mock_test_internet_connection
    ):
        yield mock_test_valid_url, mock_test_internet_connection


def test_should_access_if_has_internet_connection_and_valid_url(
        mocked_connection: tuple
) -> None:
    mocked_url, mocked_internet_connection = mocked_connection
    mocked_url.return_value = True
    mocked_internet_connection.return_value = True
    assert can_access_google_page("https://google.com/") == "Accessible"


def test_should_not_be_available_if_the_url_is_invalid(
        mocked_connection: tuple
) -> None:
    mock_valid_url, internet_mock = mocked_connection
    mock_valid_url.return_value = False
    internet_mock.return_value = True
    assert can_access_google_page("https://google.com/") == "Not accessible"


def test_should_no_access_if_not_internet_connection(
        mocked_connection: tuple
) -> None:
    mock_valid_url, internet_mock = mocked_connection
    mock_valid_url.return_value = True
    internet_mock.return_value = False
    assert can_access_google_page("https://google.com/") == "Not accessible"


def test_no_access_no_connection_internet_and_invalid_url(
        mocked_connection: tuple
) -> None:
    mock_valid_url, internet_mock = mocked_connection
    mock_valid_url.return_value = False
    internet_mock.return_value = False
    assert can_access_google_page("https://google.com/") == "Not accessible"
