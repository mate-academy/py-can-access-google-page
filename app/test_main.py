import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_valid_google_url_return, "
    "mock_has_internet_connection_return, "
    "expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        mock_valid_google_url_return: bool,
        mock_has_internet_connection_return: bool,
        expected_result: str) -> None:
    with mock.patch(
            "app.main.valid_google_url",
            return_value=mock_valid_google_url_return):
        with mock.patch(
                "app.main.has_internet_connection",
                return_value=mock_has_internet_connection_return):
            url = (
                "https://www.google.com"
                if mock_valid_google_url_return
                else "https://invalid-url.com"
            )
            result = can_access_google_page(url)
            assert result == expected_result
