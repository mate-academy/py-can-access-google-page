from unittest.mock import patch

import pytest

from app.main import can_access_google_page


@pytest.fixture
def mocked_functions() -> None:
    with patch("app.main.valid_google_url") as mocked_google, \
            patch("app.main.has_internet_connection") as mocked_internet:
        yield mocked_google, mocked_internet


@pytest.mark.parametrize(
    "valid_url,connection_status,access",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="test 'accessible' if url is valid and connected"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="test 'not accessible' if url is invalid but connected"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="test 'not accessible' if url is valid but disconnected"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="test 'not accessible' if url is invalid and disconnected"
        )
    ]
)
def test_valid_working_connection_function_and_access_google_function(
        valid_url: bool,
        connection_status: bool,
        access: str,
        mocked_functions: type
) -> None:
    mocked_google, mocked_internet = mocked_functions
    mocked_google.return_value = valid_url
    mocked_internet.return_value = connection_status

    assert can_access_google_page("url") == access
