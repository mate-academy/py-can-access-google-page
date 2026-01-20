import pytest

from unittest import mock
from unittest.mock import Mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_connection() -> Mock:
    with mock.patch(
            "app.main.has_internet_connection"
    ) as mock_connection:
        yield mock_connection


@pytest.fixture()
def mocked_valid_url() -> Mock:
    with mock.patch(
            "app.main.valid_google_url"
    ) as mock_url:
        yield mock_url


@pytest.mark.parametrize(
    "valid_connection,valid_url,expected_result",
    [
        pytest.param(
            False,
            False,
            "Not accessible",
            id="test_invalid_url_and_connect"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="test_valid_url_invalid_connect"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="test_invalid_url_valid_connect"
        ),
        pytest.param(
            True,
            True,
            "Accessible",
            id="test_valid_url_and_connect"
        )
    ]
)
def test_can_access(
        valid_connection: bool,
        valid_url: bool,
        expected_result: str,
        mocked_connection: Mock,
        mocked_valid_url: Mock
) -> None:
    mocked_connection.return_value = valid_connection
    mocked_valid_url.return_value = valid_url

    can_access_result = can_access_google_page("https://www.google.com/")

    assert can_access_result == expected_result


def test_func_called(
        mocked_connection: Mock,
        mocked_valid_url: Mock
) -> None:
    can_access_google_page("https://www.google.com/")

    mocked_connection.assert_called_once()
    mocked_valid_url.assert_called_once()
