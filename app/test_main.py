import pytest

from app.main import can_access_google_page

from unittest import mock


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_validation:
        yield mock_validation


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_function_valid_google_url_was_called_with_url(
        mocked_valid_google_url: callable
) -> None:
    can_access_google_page("https://www.etf.com/mobile")
    mocked_valid_google_url.assert_called_once_with(
        "https://www.etf.com/mobile"
    )


def test_function_has_internet_connection_was_called(
        mocked_has_internet_connection: callable
) -> None:
    can_access_google_page("https://www.etf.com/mobile")
    mocked_has_internet_connection.assert_called_once()


@pytest.mark.parametrize(
    "first_mock,second_mock,result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "should return 'Accessible' when url is valid and connection exists",
        "should return 'Not accessible' when url invalid, connection exists",
        "should return 'Not accessible' when url is valid and "
        "connection doesn't exist",
        "should return 'Not accessible' when url is invalid and "
        "connection doesn't exist",
    ]
)
def test_function_with_different_values_of_url_and_connection_functions(
        first_mock: bool,
        second_mock: bool,
        result: str,
        mocked_valid_google_url: callable,
        mocked_has_internet_connection: callable
) -> None:
    mocked_valid_google_url.return_value = first_mock
    mocked_has_internet_connection.return_value = second_mock
    assert can_access_google_page("https://www.etf.com/mobile") == result
