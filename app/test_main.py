import pytest
from unittest import mock

from app.main import can_access_google_page


test_url = "url"


@pytest.fixture()
def mocked_connection_and_valid_url_functions() -> tuple:
    with (
        mock.patch("app.main.has_internet_connection") as mocked_connection,
        mock.patch("app.main.valid_google_url") as mocked_valid_url
    ):
        yield mocked_connection, mocked_valid_url


def test_inner_functions_should_be_called(
        mocked_connection_and_valid_url_functions: tuple
) -> None:
    mock_connection, mock_valid_url = mocked_connection_and_valid_url_functions

    can_access_google_page(test_url)
    mock_connection.assert_called_once()
    mock_valid_url.assert_called_once_with(test_url)


@pytest.mark.parametrize(
    "connection_func_result,valid_url_func_result,expected_value",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
    ],
    ids=[
        "accessible",
        "not accessible",
        "not accessible",
        "not accessible"
    ]
)
def test_can_access_google_page(
        connection_func_result: bool,
        valid_url_func_result: bool,
        expected_value: str,
        mocked_connection_and_valid_url_functions: tuple
) -> None:
    mock_connection, mock_valid_url = mocked_connection_and_valid_url_functions

    mock_connection.return_value = connection_func_result
    mock_valid_url.return_value = valid_url_func_result

    assert can_access_google_page(test_url) == expected_value
