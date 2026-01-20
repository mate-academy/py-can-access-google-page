from app.main import can_access_google_page
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "is_internet_connection, is_access, expected",
    [
        pytest.param(
            True, True, "Accessible",
            id="has internet connection and validation"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="no internet connection"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="without validation"
        ),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_validation(mock_connected,
                    mock_accessible,
                    is_internet_connection,
                    is_access,
                    expected
                    ):
    mock_connected.return_value = is_internet_connection
    mock_accessible.return_value = is_access
    assert can_access_google_page("google.com") == expected
