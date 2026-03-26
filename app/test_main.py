from unittest.mock import patch
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_connection, is_valid_url, expected_result",
    [
        pytest.param(True, True, "Accessible", id="full_access"),
        pytest.param(False, True, "Not accessible", id="no_internet"),
        pytest.param(True, False, "Not accessible", id="invalid_url"),
        pytest.param(False, False, "Not accessible", id="both_fail"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_connection: any,
                                mocked_url: any,
                                has_connection: bool,
                                is_valid_url: bool,
                                expected_result: str) -> None:

    mocked_connection.return_value = has_connection
    mocked_url.return_value = is_valid_url

    result = can_access_google_page("https://google.com")

    assert result == expected_result
