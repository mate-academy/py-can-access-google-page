from unittest.mock import patch
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize(
    "google_url, internet_conn, mock_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_with_mock_parametrize_can_access_goog(
        google_url: bool,
        internet_conn: bool,
        mock_result: str,
) -> None:
    with (
        patch("app.main.has_internet_connection") as mock_internet,
        patch("app.main.valid_google_url") as mock_googl_url
    ):
        mock_internet.return_value = internet_conn
        mock_googl_url.return_value = google_url

    result = can_access_google_page("https://google.com")
    assert result == mock_result
