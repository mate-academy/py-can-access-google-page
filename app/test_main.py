from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_url_valid, has_connection, expected_result",
    [
        pytest.param(
            True, True, "Accessible",
            id="access if valid url and connection true"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="cannot access if invalid url and connection isn't allowed"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="cannot access if invalid url and valid connection"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="cannot access if valid url and invalid connection"
        ),

    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page(
        mocked_has_internet_connection: object,
        mocked_access_google_page: object,
        is_url_valid: bool,
        has_connection: bool,
        expected_result: str,
) -> None:
    mocked_has_internet_connection.return_value = has_connection
    mocked_access_google_page.return_value = is_url_valid
    assert can_access_google_page(url=None) == expected_result
