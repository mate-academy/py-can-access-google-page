import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_internet_connection() -> mock.Mock:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


@pytest.fixture()
def mocked_validation_url() -> mock.Mock:
    with mock.patch("app.main.valid_google_url") as mock_validation:
        yield mock_validation


@pytest.mark.parametrize(
    "url,connection,validation,expected_result",
    [
        pytest.param(
            "https://github.com", False, False, "Not accessible",
            id="connection is 'False', validation is 'False'"
        ),
        pytest.param(
            "https://github.com", True, False, "Not accessible",
            id="connection is 'True', validation is 'False'"
        ),
        pytest.param(
            "https://github.com", False, True, "Not accessible",
            id="connection is 'False', validation is 'True'"
        ),
        pytest.param(
            "https://github.com", True, True, "Accessible",
            id="connection is 'True', validation is 'True'"
        ),
    ]
)
def test_can_access_google_page(
        url: str,
        connection: bool,
        validation: bool,
        mocked_internet_connection: mock.Mock,
        mocked_validation_url: mock.Mock,
        expected_result: str

) -> None:
    mocked_internet_connection.return_value = connection
    mocked_validation_url.return_value = validation
    assert can_access_google_page(url) == expected_result
