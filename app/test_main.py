import pytest
from unittest.mock import patch, MagicMock

import app.main


@pytest.mark.parametrize(
    "internet_connection_flag,response_status,expected_result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="should get access with correct url and time"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="should not get access with broken url"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="should not get access without internet connection "
        ),
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_has_internet_connection: MagicMock,
        mocked_valid_google_url: MagicMock,
        internet_connection_flag: bool,
        response_status: bool,
        expected_result: str
) -> None:
    mocked_has_internet_connection.return_value = internet_connection_flag
    mocked_valid_google_url.return_value = response_status
    assert app.main.can_access_google_page("") == expected_result
