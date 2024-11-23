import pytest

from unittest.mock import patch

from app.main import can_access_google_page


@pytest.fixture()
def mocked_environment() -> tuple:
    with (
        patch("app.main.valid_google_url") as is_url,
        patch("app.main.has_internet_connection") as is_connection
    ):
        yield is_url, is_connection


@pytest.mark.parametrize(
    "is_url_valid, is_connection_possible, expected",
    [
        pytest.param(
            True, True, "Accessible",
            id="should return Accessible if both URL and connection are valid"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="should return Not accessible if URL is invalid"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="should return Not accessible if connection is unavailable"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="should return Not accessible if both are invalid"
        ),
    ]
)
def test_can_access_google_page_func(
        mocked_environment: tuple,
        is_url_valid: bool,
        is_connection_possible: bool,
        expected: bool
) -> None:

    is_url, is_connection = mocked_environment

    is_url.return_value = is_url_valid
    is_connection.return_value = is_connection_possible

    assert can_access_google_page("") == expected


def test_should_call_once__valid_google_url__with_correct_param(
        mocked_environment: tuple) -> None:

    is_url = mocked_environment[0]
    can_access_google_page("https://www.google.com/")
    is_url.assert_called_once_with("https://www.google.com/")


def test_should_call_once__has_internet_connection_func(
        mocked_environment: tuple) -> None:

    is_connection = mocked_environment[1]
    can_access_google_page("")
    is_connection.assert_called_once()
