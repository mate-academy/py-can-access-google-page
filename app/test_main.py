from unittest import mock

import pytest
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> mock.Mock:
    with mock.patch("app.main.valid_google_url") as mock_validator:
        yield mock_validator


@pytest.fixture()
def mocked_has_internet_connection() -> mock.Mock:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


@pytest.mark.parametrize(
    "internet_connection,valid_url,expected_data",
    [
        pytest.param(
            True, True, "Accessible",
            id="connection and validator True"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="connection and validator False"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="connection True, validator False"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="connection False, validator True"
        )
    ]
)
def test_can_access_google_page(
        internet_connection: bool,
        valid_url: bool,
        expected_data: str,
        mocked_valid_google_url: mock.Mock,
        mocked_has_internet_connection: mock.Mock
) -> None:
    mocked_valid_google_url.return_value = valid_url
    mocked_has_internet_connection.return_value = internet_connection
    assert can_access_google_page("https://www.google.com/") == expected_data
