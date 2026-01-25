from unittest import mock
import pytest
from app import main


@pytest.mark.parametrize(
    "is_valid_url, is_connected, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        is_valid_url: bool,
        is_connected: bool,
        expected_result: str
) -> None:
    with mock.patch("app.main.valid_google_url") as mock_url, \
            mock.patch("app.main.has_internet_connection") as mock_conn:
        mock_url.return_value = is_valid_url
        mock_conn.return_value = is_connected

        result = main.can_access_google_page("https://google.com")

        assert result == expected_result
