from unittest.mock import patch
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize(
    "mock_goog_url, mock_internet_conn, mock_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@patch("app.main.valid_google_url")
@patch("has_internet_connection")


