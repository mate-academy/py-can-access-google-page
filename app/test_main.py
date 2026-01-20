from app.main import can_access_google_page

import pytest
from unittest.mock import patch


@pytest.mark.parametrize(
    "is_url_valid, is_internet_connection, rezult",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_google_access(
    mock_valid_url,
    mock_internet,
    is_url_valid,
    is_internet_connection,
    rezult
):
    mock_valid_url.return_value = is_url_valid
    mock_internet.return_value = is_internet_connection
    assert can_access_google_page("") == rezult
