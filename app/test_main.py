import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_connection_result, mock_url_result, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
        mock_connection_result: bool,
        mock_url_result: bool,
        expected: str
) -> None:
    with patch("app.main.has_internet_connection") as mock_has_internet, \
            patch("app.main.requests.get") as mock_requests_get:
        mock_has_internet.return_value = mock_connection_result
        mock_requests_get.return_value.status_code = 200 if mock_url_result\
            else 404

        result = can_access_google_page("http://www.google.com")
        assert result == expected, f"Expected {expected}, but got {result}"
