import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> mock.Mock:
    with mock.patch("app.main.valid_google_url") as mock_test_valid_google_url:
        yield mock_test_valid_google_url


@pytest.fixture()
def mocked_has_internet_connection() -> mock.Mock:
    with (mock.patch("app.main.has_internet_connection")
          as mock_has_internet_connection):
        yield mock_has_internet_connection


@pytest.mark.parametrize(
    "is_internet_connection,is_url_valid,expected_message",
    [
        pytest.param(True, True, "Accessible",
                     id="should return 'Accessible' when both url_validation"
                        " and internet_connection are True"),
        pytest.param(False, True, "Not accessible",
                     id="should return 'Not accessible' "
                        "when internet_connection is False"),
        pytest.param(True, False, "Not accessible",
                     id="should return 'Not accessible' "
                        "when url_validation is False"),
        pytest.param(False, False, "Not accessible",
                     id="should return 'Not accessible' "
                        "when both parameters are False")
    ]
)
def test_can_access_page_when_url_and_connection_are_true(
        mocked_valid_google_url: mock.Mock,
        mocked_has_internet_connection: mock.Mock,
        is_url_valid: bool,
        is_internet_connection: bool,
        expected_message: str
) -> None:
    mocked_has_internet_connection.return_value = is_internet_connection
    mocked_valid_google_url.return_value = is_url_valid
    assert can_access_google_page("url") == expected_message
